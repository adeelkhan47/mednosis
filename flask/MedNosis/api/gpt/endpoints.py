from http import HTTPStatus
from typing import Dict, Tuple

from flask_restx import Resource
from helpers.gpt import medical_prompt

from api.gpt import schemas

from . import api


@api.route("")
class UserList(Resource):
    @api.doc("Get gpt resposne")
    @api.expect(schemas.gpt_expect, validate=True)
    @api.marshal_list_with(schemas.gpt_response, skip_none=True)
    def post(self) -> Tuple[Dict, int]:
        """
        Get gpt resposne

        Returns:
            Response
        """
        api.logger.info("Get gpt resposne")
        success, advice = medical_prompt(api.payload["prompt"])
        if success:
            return {"question": api.payload["prompt"], "data": advice}, HTTPStatus.OK
        else:
            return {"question": api.payload["prompt"], "error": advice}, HTTPStatus.BAD_REQUEST
