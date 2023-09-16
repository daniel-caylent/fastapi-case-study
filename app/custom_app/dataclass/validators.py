"""Module that contains util methods for dataclasses validations"""
from datetime import datetime
import json

def validate_str(str_, name, min_len=0, max_len=256, allowed: list = None) -> str:
    """Validate a string exists for this value"""
    if str_ is None:
        raise Exception(
            f"Required argument is missing: {name}."
        )

    try:
        str_ = str_.strip()
    except Exception as e:
        raise Exception(
            f"{name} is invalid."
        ) from e

    if len(str_) < min_len:
        raise Exception(
            f"{name} does not meet min length requirement of {min_len} characters."
        )
    if len(str_) > max_len:
        raise Exception(
            f"{name} does not meet max length requirement of {max_len} characters."
        )

    if allowed:
        if str_ not in allowed:
            raise Exception(
                f"{name} is not one of allowed: {str(allowed).strip('[]')}."
            )

    return str_


def validate_int(
    int_, name: str, min_: int=None, max_: int=None, allowed: list=None
) -> int:
    """Validate an integer exists for this value"""
    if int_ is None:
        raise Exception(
            f"Required argument is missing: {name}."
        )

    if "." in str(int_):
        raise Exception(
            f"{name} contains an invalid integer: {int_}"
        )

    try:
        int_ = int(str(int_))
    except Exception as e:
        raise Exception(
            f"{name} is invalid: {int_}"
        ) from e

    if min_ is not None:
        if int_ < min_:
            raise Exception(f"{name} is invalid.")

    if max_ is not None:
        if int_ > max_:
            raise Exception(f"{name} is invalid.")

    if allowed:
        if int_ not in allowed:
            raise Exception(
                f"{name} must be one of {allowed}."
            )

    return int_

def validate_date(date_str, name, date_format="%Y-%m-%d"):
    """Validate date objects to be inserted into mysql"""

    if date_str is None:
        raise Exception(
            f"Required argument is missing: {name}."
        )

    try:
        date = datetime.strptime(date_str, date_format)
    except:
        raise Exception(f"Datetime is invalid for {name}. Use format: {date_format}")

    return date.strftime("%Y-%m-%d")

def validate_list(lst, name, min_len=None, max_len=None, parse=False):
    """Validate a required list"""
    if parse:
        lst = json.loads(lst)

    if type(lst) is not list:
        raise Exception(
            f"List argument is not a list: {name}."
        )

    if lst is None:
        raise Exception(
            f"Required argument is missing: {name}."
        )

    if min_len is not None:
        if len(lst) < min_len:
            raise Exception(f"List argument is too short: {name}")

    if max_len is not None:
        if len(lst) > max_len:
            raise Exception(f"List argument is too long: {name}")
    
    return lst
