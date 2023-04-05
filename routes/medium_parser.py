from flask import Blueprint, request, jsonify

# Defining a Blueprint for medium address parsing
medium_parser_bp = Blueprint('parser-medium', __name__)


# Defining an error handler for when the input address is not in the expected format
@medium_parser_bp.errorhandler(ValueError)
def handle_value_error(error):
    """
    Handles ValueError raised by the simple parser.

    Returns a JSON error response with a message describing the error.
    """
    response = {
        'error': 'Incorrect format',
        'message': str(error)
    }
    return jsonify(response), 500


# Defining a route to handle requests to parse a medium address (Case #2)
@medium_parser_bp.route('/parser-medium/', methods=['POST'])
def simple_parser():
    """
        Parses a medium address input string into its street and housenumber components.

            The function accepts a POST request with a JSON payload containing an 'input_address' field
            or a form-encoded request with an 'input_address' field.

        Returns:
            A JSON object with 'street' and 'housenumber' fields.
        """
    if request.is_json:
        input_address = request.get_json().get('input_address')
    else:
        input_address = request.form['input_address']
    input_list = input_address.split()
    numeric_value = None
    for word in input_list:
        if word.isdigit():
            numeric_value = word
    if numeric_value is None:
        raise ValueError("There is no digit/integer in the string.")
    numeric_value_idx = input_address.find(numeric_value)

    return jsonify({"street": input_address[:numeric_value_idx], "housenumber": input_address[numeric_value_idx:]})