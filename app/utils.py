import json
from functools import wraps
from flask import request
from extentions import cache


def generate_cache_key():
    key = f"cache:{request.path}:{json.dumps(request.json)}"
    return key


def cache_response(success_timeout=1728000):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            cache_key = generate_cache_key()
            result = func(*args, **kwargs)
            if result:
                if cache.get(cache_key) is None:
                    cache.set(cache_key, result, timeout=success_timeout)
            return result
        return wrapped
    return decorator