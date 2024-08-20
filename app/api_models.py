from extentions import api
from flask_restx import fields

input_data_model = api.model("InputData", {
    "tg_id": fields.List(fields.String, default=None),
    "tel": fields.List(fields.String, default=None)
})