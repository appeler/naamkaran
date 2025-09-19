Web Interfaces
==============

Naamkaran provides two web interfaces for interactive name generation: a Gradio web app and a Flask API.

Gradio Web App
--------------

The Gradio app provides an easy-to-use web interface for generating names.

Installation
^^^^^^^^^^^^

To use the Gradio app, install naamkaran with web dependencies:

.. code-block:: bash

    pip install "naamkaran[web]"

Running the App
^^^^^^^^^^^^^^^

Start the Gradio interface:

.. code-block:: bash

    python gradio_app.py

This will launch a web interface accessible at ``http://localhost:7860`` where you can:

* Select starting and ending letters
* Choose gender
* Set temperature and maximum length
* Generate and view names interactively

Online Demo
^^^^^^^^^^^

You can try the Gradio app online at: `Naamkaran on Hugging Face <https://huggingface.co/spaces/sixtyfold/generate_names>`__

Flask API
---------

The Flask API provides a REST interface for programmatic access.

Running the API
^^^^^^^^^^^^^^^

Start the Flask server:

.. code-block:: bash

    python flask/flask_api.py

The API will be available at ``http://localhost:5000``.

API Endpoints
^^^^^^^^^^^^^

Generate Names
""""""""""""""

**Endpoint:** ``POST /generate``

**Request Body:**

.. code-block:: json

    {
        "starting_letter": "A",
        "ending_letter": "a",
        "gender": "F",
        "num_names": 5,
        "max_len": 8,
        "temperature": 0.7
    }

**Response:**

.. code-block:: json

    {
        "names": ["Anna", "Aria", "Aisha", "Alma", "Alba"],
        "parameters": {
            "starting_letter": "A",
            "ending_letter": "a",
            "gender": "F",
            "num_names": 5,
            "max_len": 8,
            "temperature": 0.7
        }
    }

Health Check
""""""""""""

**Endpoint:** ``GET /health``

**Response:**

.. code-block:: json

    {
        "status": "healthy",
        "version": "0.1.0"
    }

Usage Examples
^^^^^^^^^^^^^^

Using curl:

.. code-block:: bash

    # Generate names via API
    curl -X POST http://localhost:5000/generate \\
         -H "Content-Type: application/json" \\
         -d '{"starting_letter": "M", "gender": "M", "num_names": 3}'

    # Health check
    curl http://localhost:5000/health

Using Python requests:

.. code-block:: python

    import requests

    # Generate names
    response = requests.post('http://localhost:5000/generate', json={
        'starting_letter': 'S',
        'gender': 'F',
        'num_names': 5,
        'temperature': 0.8
    })

    data = response.json()
    print("Generated names:", data['names'])

Using JavaScript:

.. code-block:: javascript

    // Generate names via fetch API
    fetch('http://localhost:5000/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            starting_letter: 'R',
            gender: 'M',
            num_names: 4,
            temperature: 0.6
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Generated names:', data.names);
    });

Docker Deployment
-----------------

You can also run naamkaran using Docker:

.. code-block:: bash

    # Build the Docker image
    docker build -t naamkaran .

    # Run the container
    docker run -p 5000:5000 naamkaran

This will start the Flask API in a Docker container accessible at ``http://localhost:5000``.

Integration Examples
--------------------

Web Application Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Here's an example of integrating the Flask API into a web application:

.. code-block:: html

    <!DOCTYPE html>
    <html>
    <head>
        <title>Name Generator</title>
    </head>
    <body>
        <h1>Generate Names</h1>
        <form id="nameForm">
            <label for="starting_letter">Starting Letter:</label>
            <input type="text" id="starting_letter" maxlength="1">

            <label for="gender">Gender:</label>
            <select id="gender">
                <option value="">Any</option>
                <option value="M">Male</option>
                <option value="F">Female</option>
            </select>

            <label for="num_names">Number of Names:</label>
            <input type="number" id="num_names" value="5" min="1" max="50">

            <button type="submit">Generate Names</button>
        </form>

        <div id="results"></div>

        <script>
            document.getElementById('nameForm').addEventListener('submit', async (e) => {
                e.preventDefault();

                const formData = {
                    starting_letter: document.getElementById('starting_letter').value || null,
                    gender: document.getElementById('gender').value || null,
                    num_names: parseInt(document.getElementById('num_names').value)
                };

                try {
                    const response = await fetch('/generate', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify(formData)
                    });

                    const data = await response.json();
                    document.getElementById('results').innerHTML =
                        '<h3>Generated Names:</h3><ul>' +
                        data.names.map(name => `<li>${name}</li>`).join('') +
                        '</ul>';
                } catch (error) {
                    console.error('Error:', error);
                }
            });
        </script>
    </body>
    </html>

Mobile App Integration
^^^^^^^^^^^^^^^^^^^^^^

For mobile applications, you can integrate the API using standard HTTP libraries:

.. code-block:: swift

    // iOS Swift example
    import Foundation

    struct NameRequest: Codable {
        let starting_letter: String?
        let gender: String?
        let num_names: Int
        let temperature: Double
    }

    struct NameResponse: Codable {
        let names: [String]
    }

    func generateNames(request: NameRequest, completion: @escaping ([String]?) -> Void) {
        guard let url = URL(string: "http://localhost:5000/generate") else { return }

        var urlRequest = URLRequest(url: url)
        urlRequest.httpMethod = "POST"
        urlRequest.setValue("application/json", forHTTPHeaderField: "Content-Type")

        do {
            urlRequest.httpBody = try JSONEncoder().encode(request)
        } catch {
            completion(nil)
            return
        }

        URLSession.shared.dataTask(with: urlRequest) { data, response, error in
            guard let data = data, error == nil else {
                completion(nil)
                return
            }

            do {
                let nameResponse = try JSONDecoder().decode(NameResponse.self, from: data)
                completion(nameResponse.names)
            } catch {
                completion(nil)
            }
        }.resume()
    }
