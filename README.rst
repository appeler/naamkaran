naamkaran: Generative model for names
-------------------------------------

.. image:: https://github.com/appeler/naamkaran/workflows/test/badge.svg
    :target: https://github.com/appeler/naamkaran/actions?query=workflow%3Atest
.. image:: https://img.shields.io/pypi/v/naamkaran.svg
    :target: https://pypi.python.org/pypi/naamkaran
.. image:: https://pepy.tech/badge/naamkaran
    :target: https://pepy.tech/project/naamkaran

Naamkaran is a generative model for names. It is a simple character-level RNN that predicts 
the next character given the previous characters. The model is trained on a list of names from 
FL Voter Registration Data and can be used to generate new names.

Installation
------------

Naamkaran can be installed from PyPI using pip:

.. code-block:: bash

    pip install naamkaran

General API
-----------

The general API for naamkaran is as follows:

:: 

    # naamkaran is the package name
    from naamkaran.generate import generate_names

    # generate_names is the function that generates names

    positional arguments:
      start_letter  The letter to start the name with

    optional arguments:
        end_letter  The letter to end the name with (default: None)
        how_many    The number of names to generate (default: 1)
        max_length  The maximum length of the name (default: 5)
        gender      The gender of the name (default: "M")
        temperature The temperature of the model (default: 0.5)

    # generate 10 names starting with 'A'
    generate_names('A', how_many=10)
    ['Allis', 'Alber', 'Aderi', 'Albri', 'Alawa', 
    'Arver', 'Agnee', 'Anous', 'Areyd', 'Adria']


    # generate 10 names starting with 'A' and ending with 'n'
    generate_names('B', end_letter='n', how_many=10)
    ['Brian', 'Beran', 'Burin', 'Bahan', 'Balin',
    'Bounn', 'Baran', 'Balan', 'Belin', 'Brion']

    # generate 5 names starting with 'B' and ending with 'n' with a maximum length of 4
    generate_names('B', end_letter='n', how_many=5, max_length=4)
    ['Bern', 'Bren', 'Bran', 'Bonn', 'Brun']

    # generate 10 names starting with 'A' and ending with 'n' with a maximum length of 6
    # and a temperature of 0.5
    generate_names('D', end_letter='d', how_many=5, max_length=6, temperature=0.5)
    ['Derayd', 'Davind', 'Deland', 'Denild', 'David']

    # generate 10 female names starting with 'A' and ending with 'n' with a maximum length of 5
    # and a temperature of 0.5
    generate_names('A', end_letter='e', how_many=10, max_length=5, gender="F", temperature=0.5)
    ['Annhe', 'Annie', 'Altre', 'Anne', 'Ashle',
    'Arine', 'Anice', 'Andre', 'Anale', 'Allie']


Data
----

The data used to train the model is from the Florida Voter Registration Data from early 2022.
The data is available here - `Florida voter registration database <http://dx.doi.org/10.7910/DVN/UBIG3F>`__


Authors
-------

Rajashekar Chintalapati and Gaurav Sood

Contributing
------------

Contributions are welcome. Please open an issue if you find a bug or have a feature request.

License
-------

The package is released under the `MIT License <https://opensource.org/licenses/MIT>`_.