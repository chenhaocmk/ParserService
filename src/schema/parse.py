"""
Schema of parsing functions
"""


INPUT_SCHEMA = {
    'requiredProperties': ['input_string'],
    'properties': {
        'input_string': {
            'validFunc': lambda x: isinstance(x, str)
        }
    },
    'additionalPropertiesAllowed': False
}


OUTPUT_SCHEMA = {
    'requiredProperties': ['item'],
    'properties': {
        'number': {
            'validFunc': lambda x: isinstance(x, str)
        },
        'unit': {
            'validFunc': lambda x: isinstance(x, str)
        },
        'item': {
            'validFunc': lambda x: isinstance(x, str)
        }
    },
    'additionalPropertiesAllowed': False
}
