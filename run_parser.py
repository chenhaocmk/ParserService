from flask import Flask, jsonify, request

from src.util.schemaValidation import validate_json, validate_input_schema, validate_output_schema
import src.schema.parse as s_parse
from src.model.parser import IngredientParser


app = Flask(__name__)


@app.route('/parse/ingredient', methods=['POST'])
@validate_json
@validate_input_schema(s_parse.INPUT_SCHEMA)
@validate_output_schema(s_parse.OUTPUT_SCHEMA)
def parse_string():
    input_string = request.json['input_string']
    return IngredientParser().parse(input_string)


app.run(host='127.0.0.1', port=8122)
