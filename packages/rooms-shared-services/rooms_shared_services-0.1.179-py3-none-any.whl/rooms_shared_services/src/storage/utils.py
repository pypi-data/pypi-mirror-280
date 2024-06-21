import logging
from typing import Any
from rooms_shared_services.src.encoders.json import RawDynamodbEncoder
import json
from decimal import Decimal
from uuid import UUID
from datetime import datetime
from boto3.dynamodb.types import TypeSerializer, TypeDeserializer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

type_serializer = TypeSerializer()
type_deserializer = TypeDeserializer()


def dump_value_dict(data_dict: dict, dynamodb_format: bool = False, json_format: bool = False) -> str | dict:
    data_dict = {item_key: formatted_value for item_key, item_value in data_dict.items() if (formatted_value := convert_to_supported_format(item_value)) is not None}
    if dynamodb_format:
        data_dict = {item_key: serialize_value(item_value) for item_key, item_value in data_dict.items()}
    if json_format:
        return convert_to_json(data_dict)
    return data_dict


def load_value_json(value_json: str) -> dict:
    value_dict = json.loads(value_json)
    return parse_serialized_dict(value_dict=value_dict)

    
def parse_serialized_dict(value_dict: dict) -> dict:
    value_dict = {item_key: type_deserializer.deserialize(item_value) for item_key, item_value in value_dict.items()}
    return {item_key: convert_from_supported_formats(item_value) for item_key, item_value in value_dict.items()}


def convert_from_supported_formats(item_value: Any) -> Any:
    match item_value:
        case Decimal():
            float_value = float(item_value)
            int_value = int(item_value)
            if float_value == int_value:
                converted_value = int_value
            else:
                converted_value = float_value
        case _:
            converted_value = item_value
    return converted_value


def convert_to_json(data_dict: dict) -> str:
    return json.dumps(data_dict, indent=4)


def serialize_value(item_value: Any) -> dict:
    return type_serializer.serialize(item_value)


def convert_to_supported_format(item_value: Any):
    match item_value:
        case UUID():
            formatted_value = str(item_value)
        case float():
            formatted_value = Decimal(str(item_value))
        case datetime():
            formatted_value = item_value.isoformat()
        case list():
            formatted_value = [convert_to_supported_format(item_value_elem) for item_value_elem in item_value]
        case set():
            formatted_value = {convert_to_supported_format(item_value_elem) for item_value_elem in item_value}
        case dict():
            formatted_value = {item_value_key: convert_to_supported_format(item_value_value) for item_value_key, item_value_value in item_value.items()}
        case _:
            formatted_value = item_value            
    return formatted_value
