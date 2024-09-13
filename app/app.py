import os

from flask import Flask
from extentions import api, cache
from resources import ns


def create_app():
    app = Flask(__name__)
    api.init_app(app)
    api.add_namespace(ns)
    register_extension(app)
    return app


def register_extension(app):
    cache.init_app(app, config={"CACHE_TYPE": os.environ.get('CACHE_TYPE', 'redis'),
                                "CACHE_REDIS_HOST": os.environ.get('CACHE_REDIS_HOST', 'redis'),
                                "CACHE_REDIS_PORT": os.environ.get('CACHE_REDIS_PORT', 6397),
                                "CACHE_REDIS_DB": os.environ.get('CACHE_REDIS_DB', 0),
                                "CACHE_REDIS_URL": os.environ.get('CACHE_REDIS_URL', 'redis://redis:6379/0'),
                                "CACHE_DEFAULT_TIMEOUT": os.environ.get('CACHE_DEFAULT_TIMEOUT', 10000)})


if __name__ == "__main__":
    app = create_app()
    while True:
        app.run(host="0.0.0.0", port=3000, debug=True)