from typing import Any

from flask import Flask, jsonify, request
from naamkaran.generate import generate_names

app = Flask(__name__)


@app.route("/generate_names", methods=["POST"])
def generate_names_api() -> dict[str, Any] | tuple[Any, int]:
    # Get request data as JSON
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    # Extract parameters from JSON data or set default values
    start_letter = str(data.get("start_letter", "a"))
    end_letter = data.get("end_letter", None)
    if end_letter is not None:
        end_letter = str(end_letter)

    try:
        how_many = int(data.get("how_many", 1))
        max_length = int(data.get("max_length", 5))
        temperature = float(data.get("temperature", 0.5))
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid parameter types"}), 400

    gender = str(data.get("gender", "M"))

    # Validate parameters
    if gender not in ["M", "F"]:
        return jsonify({"error": "Gender must be 'M' or 'F'"}), 400
    if how_many < 1 or how_many > 100:
        return jsonify({"error": "how_many must be between 1 and 100"}), 400
    if max_length < 1 or max_length > 20:
        return jsonify({"error": "max_length must be between 1 and 20"}), 400
    if temperature < 0.1 or temperature > 2.0:
        return jsonify({"error": "temperature must be between 0.1 and 2.0"}), 400

    try:
        # Generate names using the provided parameters
        names = generate_names(
            start_letter=start_letter,
            end_letter=end_letter,
            how_many=how_many,
            max_length=max_length,
            gender=gender,
            temperature=temperature,
        )
        # Return the generated names as JSON
        return {"names": names}
    except Exception as e:
        return jsonify({"error": f"Name generation failed: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=False)
