from extentions import api
from flask_restx import fields

accounts_model = api.model("TgAccount", {
    "id": fields.String,
    "tel": fields.String,
    "info": fields.String,
})

input_data_model = api.model("InputData", {
    "tg_id": fields.List(fields.String)
})


non_data_model = api.model("NonDataModel", {
    "query": fields.List(fields.String),
    "tel": fields.String,
    "data": fields.List(fields.Raw),
})