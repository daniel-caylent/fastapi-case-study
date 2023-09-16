"""Module that contains methods for dataclasses encoding"""
import dataclasses
import datetime
from decimal import Decimal


def encode(obj):
    """Convert dataclass objects to dicts"""
    if isinstance(obj, list):
        for idx, _ in enumerate(obj):
            obj[idx] = encode(obj[idx])
    
    elif isinstance(obj, dict):
       for key in obj.keys():
          obj[key] = encode(obj[key])

    elif dataclasses.is_dataclass(obj):
        return dataclasses.asdict(obj)
    
    elif isinstance(obj, Decimal):
        return int(obj)
    
    elif isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
        return str(obj)

    return obj
