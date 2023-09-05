from flask import Flask, request, jsonify
from naamkaran.generate import generate_names

app = Flask(__name__)

@app.route('/generate_names', methods=['POST'])
def generate_names_api():
    # Get request data as JSON
    data = request.get_json()

    # Extract parameters from JSON data or set default values
    start_letter = data.get('start_letter', 'a')
    end_letter = data.get('end_letter', None)
    how_many = data.get('how_many', 1)
    max_length = data.get('max_length', 5)
    gender = data.get('gender', 'M')
    temperature = data.get('temperature', 0.5)

    # Generate names using the provided parameters
    names = generate_names(
        start_letter=start_letter,
        end_letter=end_letter,
        how_many=how_many,
        max_length=max_length,
        gender=gender,
        temperature=temperature
    )

    # Return the generated names as JSON
    return jsonify(names)

if __name__ == '__main__':
    app.run(debug=True)
