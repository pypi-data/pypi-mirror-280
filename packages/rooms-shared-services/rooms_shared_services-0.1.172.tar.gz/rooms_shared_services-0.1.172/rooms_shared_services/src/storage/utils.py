from typing import Any
from rooms_shared_services.src.encoders.json import RawDynamodbEncoder
import json
from decimal import Decimal
from uuid import UUID


def convert_to_raw(data_dict: dict, root_level: bool = False) -> dict:
    return {
        item_key: convert_to_raw_value(item_value, root_level=root_level)
        for (item_key, item_value) in data_dict.items()
    }

def convert_to_raw_value(item_value: Any, root_level: bool = False) -> dict | list:
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
