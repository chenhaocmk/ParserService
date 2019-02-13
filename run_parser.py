import string
import sys


# def assert_works(input, expectation):
#     parser = IngredientParser()
#     result = parser.parse(input)
#     assert result == expectation
#
#
# assert_works("1 cup vinegar", {"n": 1,
#                                "u": "cup",
#                                "f": "vinegar"})
# assert_works("15 g. all purpose flour", {"n": 15,
#                                          "u": "g",
#                                          "f": "all purpose flour"})
# assert_works("doesn't have an ingredient", {"n": None,
#                                             "u": None,
#                                             "f": "doesn't have an ingredient"})


from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route('/')
def hello():
    ingredient = request.args.get('ing')
    parser = IngredientParser()
    return jsonify(parser.parse(ingredient))

app.run()

