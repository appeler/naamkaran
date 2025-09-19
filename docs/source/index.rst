naamkaran: Generative Model for Names
====================================

.. image:: https://github.com/appeler/naamkaran/actions/workflows/python-package.yml/badge.svg
    :target: https://github.com/appeler/naamkaran/actions?query=workflow%3Apython-package
    :alt: Tests

.. image:: https://img.shields.io/pypi/v/naamkaran.svg
    :target: https://pypi.python.org/pypi/naamkaran
    :alt: PyPI Version

.. image:: https://static.pepy.tech/badge/naamkaran
    :target: https://pepy.tech/project/naamkaran
    :alt: Downloads

Naamkaran is a generative model for names built with PyTorch. It uses a character-level RNN (LSTM) trained on Florida Voter Registration Data to generate names based on starting letter, ending letter, gender, and other parameters.

Features
--------

* **Character-level LSTM**: Deep learning model trained on real name data
* **Flexible generation**: Generate names by starting letter, ending letter, gender, and length
* **Multiple interfaces**: Python API, command-line tool, Gradio web app, and Flask API
* **High-quality output**: Names that look and sound realistic
* **Fast inference**: Optimized for quick name generation

Quick Start
-----------

Install naamkaran:

.. code-block:: bash

    pip install naamkaran

Generate names programmatically:

.. code-block:: python

    from naamkaran.generate import generate_names

    # Generate 5 female names starting with 'A' and ending with 'a'
    names = generate_names(
        starting_letter='A',
        ending_letter='a',
        gender='F',
        num_names=5,
        max_len=8,
        temperature=0.7
    )
    print(names)

Or use the command line:

.. code-block:: bash

    generate_names -s A -e a -g F -n 5 -m 8 -t 0.7

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :caption: User Guide:

   installation
   quickstart
   examples
   web_interfaces

.. toctree::
   :maxdepth: 2
   :caption: API Reference:

   api/modules
   api/naamkaran

.. toctree::
   :maxdepth: 1
   :caption: Development:

   contributing
   changelog

Indices and Tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
