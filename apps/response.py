from flask import jsonify
from typing import Dict, Union, Any

from .messages import (
    MSG_INVALID_DATA,
    MSG_EXCEPTION,
    MSG_DOES_NOT_EXIST,
    MSG_ALREADY_EXISTS
)


def resp_data_invalid(resource: str, errors: dict, msg: str = MSG_INVALID_DATA) -> Dict[str, Union[str, dict, int]]:
    """
    Response 422 Unprocessable Entity
    :param resource:
    :param errors:
    :param msg:
    :return: response 422 -> Dicionario com campos resource, message,  errors e status_code
    """

    if not isinstance(resource, str):
        raise ValueError('O recurso precisa ser uma String')

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'errors': errors,
    })

    resp.status_code = 422

    return resp


def resp_exception(resource: str, description: str = '', msg: str = MSG_EXCEPTION) -> Dict[str, Union[str, int]]:
    """
    Response 500
    :param resource:
    :param description:
    :param msg:
    :return: response 500 -> Dicionario com campos resource, message,  description e status_code
    """

    if not isinstance(resource, str):
        raise ValueError("O recurso precisa ser uma string")

    resp = jsonify({
        'resource': resource,
        'message': msg,
        'description': description
    })

    resp.status_code = 404

    return resp


def resp_already_exists(resource: str, description: str) -> Dict[str, Union[str, int]]:
    """
    Response 400
    :param resource:
    :param description:
    :return: response 400 -> Dicionario com campos resource, message e status_code
    """

    if not isinstance(resource, str):
        raise ValueError("O recurso precisa ser uma string")

    resp = jsonify({
        'resource': resource,
        'message': MSG_ALREADY_EXISTS.format(description)
    })

    resp.status_code = 400

    return resp


def resp_ok(resource: str, message: str, data: Dict[str, Any] = None, **kwargs) -> Dict[str, Union[str, int, Any]]:
    """
    Response 200
    :param resource:
    :param message:
    :param data:
    :param kwargs: Parametros extras
    :return: response 200 -> Dicionario com campos resource, message, data,  status_code e parametros extras
    """

    response = {
        'resource': resource,
        'message': message
    }

    if data:
        response['data'] = data

    if kwargs:
        response.update(kwargs)

    resp = jsonify(response)
    resp.status_code = 200

    return resp
