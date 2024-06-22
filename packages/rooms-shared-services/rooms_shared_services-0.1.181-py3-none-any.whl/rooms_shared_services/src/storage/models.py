import json
from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import Any, Literal, get_args
from uuid import uuid4, UUID
from rooms_shared_services.src.storage.utils import dump_value_dict, parse_serialized_dict, convert_from_supported_formats
from typing import Self

from pydantic import BaseModel, ConfigDict
from pydantic.fields import FieldInfo

from rooms_shared_services.src.encoders.json import RawDynamodbEncoder
from rooms_shared_services.src.models.base import Unset

UNSET = Literal["UNSET"]


class BaseDynamodbModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    
    def __eq__(self, other: Any):
        if not isinstance(other, self.__class__):
            return False
        return self.model_dump(exclude_unset=True) == other.model_dump(exclude_unset=True)

    @classmethod
    def create_with_id(cls, **attributes):
        model_id = uuid4()
        value_dict = {"id": model_id, **attributes}
        return cls.model_validate(value_dict)

    def convert_value(self, item_value, exclude_unset: bool):
        match item_value:
            case BaseDynamodbModel():
                converted_item_value = item_value.dynamodb_dump(exclude_unset=exclude_unset)
            case int():
                converted_item_value = Decimal(item_value)
            case float():
                converted_item_value = Decimal(str(item_value))
            case dict():
                converted_item_value = self.convert_dict(item_value, exclude_unset=exclude_unset)
            case list():
                converted_item_value = [
                    self.convert_value(item_value_item, exclude_unset=exclude_unset) for item_value_item in item_value
                ]
            case Enum():
                converted_item_value = item_value.name
            case datetime():
                converted_item_value = item_value.isoformat()
            case _:
                converted_item_value = str(item_value)
        return converted_item_value

    def convert_to_raw(self, data_dict: dict, root_level: bool = False) -> dict:
        return {
            item_key: self.convert_to_raw_value(item_value, root_level=root_level)
            for (item_key, item_value) in data_dict.items()
        }

    def convert_to_raw_value(self, item_value: Any, root_level: bool = False):
        match item_value:
            case Decimal():
                item_value_dict = {"N": str(item_value)}
            case dict():
                item_value_dict = {"M": json.dumps(item_value, cls=RawDynamodbEncoder)}
            case list():
                item_value_dict = {"L": json.dumps(item_value, cls=RawDynamodbEncoder)}
            case str():
                item_value_dict = {"S": item_value}
            case bool():
                item_value_dict = {"BOOL": "true" if item_value else "false"}
            case None:
                item_value_dict = {"NULL": ""}
            case UUID():
                item_value_dict = {"S": str(item_value)}                
            case _:
                raise ValueError("Invalid item value type")
        return item_value_dict if root_level else list(item_value_dict.values()).pop()

    def convert_dict(self, item_dict: dict, exclude_unset: bool):
        return {
            item_key: self.convert_value(item_value, exclude_unset=exclude_unset)
            for (item_key, item_value) in item_dict.items()
        }

    def dynamodb_dump(self, exclude_unset: bool = True, include: set[str] | None = None, raw: bool = False):
        item_dict = self.model_dump(exclude_unset=exclude_unset, include=include)
        return dump_value_dict(data_dict=item_dict, dynamodb_format=raw, json_format=False)

    @classmethod
    def validate_value(cls, item_value: Any) -> Any:
        match item_value:
            case list():
                validated_value = [cls.validate_value(item_value=product_elem) for product_elem in item_value]
            case "None":
                validated_value = None
            case dict():
                return {
                    elem_key: cls.validate_value(item_value=elem_value) for elem_key, elem_value in item_value.items()
                }
            case _:
                validated_value = item_value
        return validated_value

    @classmethod
    def parse_raw_record_attribute(cls, attr_dict: dict[str, str]) -> Any:
        item_key, item_value = list(attr_dict.items()).pop()
        match item_key:
            case "S":
                res = str(item_value)
            case "N":
                res = float(item_value)
            case "B":
                res = item_value
            case "BOOL":
                res = item_value == "true"
            case "NULL":
                res = None
            case "M" | "L":
                res = json.loads(item_value)
            case "SS" | "NS" | "BS":
                res = set(item_value)
            case _:
                raise ValueError("Invalid data type")
        return res

    @classmethod
    def validate_dynamodb_item(cls, data_dict: dict, from_raw: bool = False) -> Self:
        if from_raw:
            data_dict = parse_serialized_dict(value_dict=data_dict)
        data_dict = {item_key: cls.validate_value(item_value) for item_key, item_value in data_dict.items()}
        return cls.model_validate(data_dict)
    
    @classmethod
    def validate_stored_item_with_none(cls, data_dict: dict, from_raw: bool = False):
        value_dict = {key: data_dict.get(key) for key in cls.model_fields}
        return cls.validate_dynamodb_item(data_dict=value_dict, from_raw=from_raw)
    
    @classmethod
    def validate_item(cls, item_dict: dict, include_unsets: bool = False, include_nones: bool = True) -> Self:
        """Create new data model from provided data dict. 
        Substitute absent values with Unset instances if include_unsets is True.
        Substitute absent values with None values if include_nones is True.
        At most one of (include_unsets, include_nones) must be True.

        Args:
            item_dict (dict): _description_
            include_unsets (bool): _description_. Defaults to False.
            include_none (bool): _description_. Defaults to True.

        Returns:
            Self: An instance of the class.
        """
        if include_unsets + include_nones == 2:
            raise ValueError("At most one of (include_unsets, include_nones) must be True")
        model_fields = cls.model_fields
        field_names = model_fields.keys()
        key_value_dict = {}
        if include_unsets:
            key_value_dict.update({field_name: Unset() for field_name in field_names})
        if include_nones:
            key_value_dict.update({field_name: None for field_name in field_names})
        key_value_dict.update(item_dict)
        key_value_dict = {item_key: convert_from_supported_formats(item_value) 
                          for item_key, item_value in key_value_dict.items()}
        key_value_dict = {item_key: cls.validate_item_value(item_key=item_key, item_value=item_value, model_fields=model_fields, include_unsets=include_unsets, include_nones=include_nones) for item_key, item_value in key_value_dict.items()}
        return cls.model_validate(key_value_dict)
    
    @classmethod
    def validate_item_value(
        cls,
        item_key: str,
        item_value: Any,
        model_fields: dict,
        include_unsets: bool = False,
        include_nones: bool = True
    ):
        if item_key in model_fields:
            field_info: FieldInfo = model_fields[item_key]
            for type_elem in get_args(field_info.annotation):
                if issubclass(type_elem, BaseDynamodbModel) and isinstance(item_value, dict):
                    return cls.validate_item(
                        item_dict=item_value,
                        include_unsets=include_unsets,
                        include_nones=include_nones
                    )
        return item_value

    @classmethod
    def validate_from_raw_record(cls, data_dict: dict):
        key_value_dict = {}
        for product_key, product_value in data_dict.items():
            validated_key = product_key
            match product_key:
                case _:
                    pass
            validated_value = cls.validate_value(item_value=product_value)
            key_value_dict.update({validated_key: validated_value})

        return cls.model_validate(key_value_dict)
