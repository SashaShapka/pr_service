import datetime
import hashlib
import os
import httpx
from werkzeug.exceptions import GatewayTimeout

from flask_restx import Resource, Namespace
from api_models import input_data_model

from datetime import datetime

ns = Namespace("api/tg_pr")


@ns.route("/status")
class StatusAPi(Resource):
    def get(self):
        return {"status": "OK"}


def gen_kluch():
    salt = os.getenv("SALT")
    gen_kluch = hashlib.md5(
        (salt + datetime.now().strftime('%d.%m.%Y')).encode('utf-8')).hexdigest()
    return gen_kluch


@ns.route("/")
class ProxyAPi(Resource):
    @ns.expect(input_data_model)
    def post(self):

        kluch = gen_kluch()
        token = os.getenv("TOKEN")
        target_url = os.getenv("TARGET_URL")
        tg_ids = ns.payload.get("tg_id")
        tel_numbers = ns.payload.get("tel")
        headers = {
            'Content-Type': 'application/json',
            'token': token,
            'kluch': kluch
        }
        data = {"tg_id": tg_ids} if tg_ids else {"tel": tel_numbers} if tel_numbers else {}
        timeout = httpx.Timeout(15.0)
        try:
            with httpx.Client(timeout=timeout) as client:
                response = client.post(target_url, headers=headers, json=data)
                response.raise_for_status()
            return response.json()
        except httpx.RequestError as exc:
            if isinstance(exc, httpx.TimeoutException):
                raise GatewayTimeout
