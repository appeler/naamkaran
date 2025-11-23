import requests

# API endpoint URL
url = "http://127.0.0.1:5000/generate_names"  # Update with your actual URL if needed

# Request payload (JSON data)
data = {"start_letter": "A", "how_many": 10}

# Send a POST request to the API
response = requests.post(url, json=data, timeout=30)  # nosec B113

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Parse the JSON response
    generated_names = response.json()

    # Print the generated names
    print("Generated Names:")
    for name in generated_names:
        print(name)
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
