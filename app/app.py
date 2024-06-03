from flask import Flask
from extentions import api
from resources import ns
from dotenv import load_dotenv


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    api.add_namespace(ns)
    return app


if __name__ == "__main__":
    app = create_app()
    while True:
        app.run(host="0.0.0.0", port=3000, debug=True)