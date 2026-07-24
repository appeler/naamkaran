Installation
============

Requirements
------------

Naamkaran requires Python 3.9 or higher and the following dependencies:

* PyTorch >= 2.0.0
* pandas >= 2.0.0
* joblib >= 1.3.0
* scikit-learn >= 1.3.0

Install from PyPI
-----------------

The easiest way to install naamkaran is from PyPI using pip:

.. code-block:: bash

    pip install naamkaran

For Web Interfaces
------------------

If you want to use the Gradio web app or Flask API, install with web dependencies:

.. code-block:: bash

    pip install "naamkaran[web]"

Development Installation
------------------------

For development, clone the repository and install in editable mode:

.. code-block:: bash

    git clone https://github.com/appeler/naamkaran.git
    cd naamkaran
    pip install -e ".[dev,test]"

This will install all development dependencies including pytest, black, isort, flake8, mypy, and pre-commit hooks.

Verify Installation
-------------------

To verify the installation, try generating some names:

.. code-block:: python

    from naamkaran.generate import generate_names

    names = generate_names(starting_letter='A', gender='F', num_names=3)
    print(names)

Or test the command-line interface:

.. code-block:: bash

    generate_names --help
