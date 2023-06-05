from flask_restx.fields import Integer, List, Nested, String

from . import api

gpt_expect = api.model(
    "gpt_expect",
    {
        "prompt": String(required=True),
    },
)

gpt_response = api.model(
    "gpt_response",
    {
        "question": String,
        "data": String,
        "error": String,
    },
)
