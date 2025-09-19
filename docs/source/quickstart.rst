Quick Start Guide
=================

This guide will help you get started with naamkaran quickly.

Basic Usage
-----------

Python API
^^^^^^^^^^^

The main function for generating names is :func:`naamkaran.generate.generate_names`:

.. code-block:: python

    from naamkaran.generate import generate_names

    # Generate 5 names
    names = generate_names(num_names=5)
    print(names)

You can specify various parameters to control name generation:

.. code-block:: python

    # Generate female names starting with 'A'
    names = generate_names(
        starting_letter='A',
        gender='F',
        num_names=5,
        max_len=8,
        temperature=0.7
    )

Command Line Interface
^^^^^^^^^^^^^^^^^^^^^^

Naamkaran also provides a command-line interface:

.. code-block:: bash

    # Generate 5 names
    generate_names -n 5

    # Generate female names starting with 'A' and ending with 'a'
    generate_names -s A -e a -g F -n 5 -m 8 -t 0.7

Parameters
----------

The following parameters can be used to control name generation:

* **starting_letter** (str): First letter of the name (e.g., 'A', 'B')
* **ending_letter** (str): Last letter of the name (e.g., 'a', 'n')
* **gender** (str): Gender for name generation ('M' for male, 'F' for female)
* **num_names** (int): Number of names to generate (default: 10)
* **max_len** (int): Maximum length of generated names (default: 12)
* **temperature** (float): Controls randomness (0.0-2.0, default: 0.8)

Temperature Effects
-------------------

The temperature parameter controls the creativity vs. realism trade-off:

* **Low temperature (0.1-0.5)**: More conservative, realistic names
* **Medium temperature (0.6-1.0)**: Balanced creativity and realism
* **High temperature (1.1-2.0)**: More creative, potentially unusual names

Examples
--------

Generate Conservative Names
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    conservative_names = generate_names(
        gender='M',
        temperature=0.3,
        num_names=5
    )

Generate Creative Names
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    creative_names = generate_names(
        starting_letter='Z',
        temperature=1.5,
        num_names=3
    )

Generate Names with Specific Pattern
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    pattern_names = generate_names(
        starting_letter='M',
        ending_letter='a',
        gender='F',
        max_len=6,
        num_names=10
    )
