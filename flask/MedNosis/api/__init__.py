import logging
from http import HTTPStatus

from flask import Blueprint
from flask_restx import Api
from werkzeug.exceptions import Unauthorized

from .gpt.endpoints import api as gpt_api

blueprint = Blueprint("api", __name__)

authorizations = {
    "Authorization": {
        "description": "",
        "type": "apiKey",
        "in": "header",
        "name": "Authorization",
    }
}

api = Api(
    blueprint,
    title="Mednosis API",
    version="0.1",
    description="Mednosis APIs",
    authorizations=authorizations,
    security="Authorization",
)

api.add_namespace(gpt_api)


@api.errorhandler(Unauthorized)
def handle_unauthorized_error(exception_cause):
    """
    Catch unauthorized exceptions globally and respond with 401.

    Args:
        exception_cause: Cause

    Returns:
        Response
    """
    logging.exception(exception_cause)
    return exception_cause.description, HTTPStatus.UNAUTHORIZED
