"""
Schema validation
"""

from functools import wraps

from flask import (
    jsonify,
    request,
)

__author__ = 'haochen'


class ValidationError(Exception):
    def __init__(self, message, *args, **kwargs):
        self.message = message
        super().__init__(self, *args, **kwargs)


def validate_json(f):
    """
    Decorator to validate input request is a json
    :param f: function
    :return: Wrapped function with json validation
    """
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            assert request.json
        except Exception:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kwargs)
    return wrapper


def validate_input_schema(schema_dict):
    """
    Decorator to validate input schema
    :param schema_dict: Schema dict
    :return: Decorated function with input schema validated
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                validate(request.json, schema_dict)
            except ValidationError as e:
                return jsonify({"error": e.message}), 400
            return f(*args, **kwargs)
        return wrapper
    return decorator


def validate_output_schema(schema_dict):
    """
    Decorator to validate output schema
    :param schema_dict: Schema dict
    :return: Decorated function with output schema validated
    """
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            output = f(*args, **kwargs)
            try:
                validate(output, schema_dict)
            except ValidationError as e:
                return jsonify({"error": e.message}), 500
            return jsonify(output)
        return wrapper
    return decorator


def validate(json_dict, schema_dict):
    """
    Validate json dict according to schema dict. Raise ValidationError if failed validation.
    :param json_dict: Json dict
    :param schema_dict: Schema dict
    """
    for item in schema_dict.get('requiredProperties', []):
        if item not in json_dict:
            raise ValidationError('Item "{}" required but not found.'.format(item))

    for item, value in json_dict.items():
        if item in schema_dict['properties'] and schema_dict['properties'][item].get('validFunc', None):
            if not schema_dict['properties'][item]['validFunc'](value):
                raise ValidationError('Item "{}" value invalid: "{}".'.format(item, value))
        elif not schema_dict.get('additionalPropertiesAllowed', True) and item not in schema_dict['properties']:
            raise ValidationError('Additional property not allowed: "{}"'.format(item))
