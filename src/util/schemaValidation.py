from functools import wraps
from flask import (
    current_app,
    jsonify,
    request,
)


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            request.json
        except BadRequest as e:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kwargs)
    return wrapper


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                validate(request.json, current_app.config[schema_name])
            except ValidationError as e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kwargs)
        return wrapper
    return decorator
