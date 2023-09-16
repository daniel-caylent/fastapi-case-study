"""Module that defines a standard response for all lambdas that serve the API Gateway"""

import json

from dataclass.encoder import encode


def response(code: int, id_: str, data=None, **kwargs):
    """Generate json encodable and consistent responses for lambda functions"""

    response_ = {
        "statusCode": code,
        "isBase64Encoded": False,
    }

    body = {"eventId": id_, **kwargs}

    if data is not None:
        body["data"] = encode(data)

    response_["body"] = json.dumps(body)
    return response_
