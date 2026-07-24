Examples
========

This page provides detailed examples of using naamkaran for various name generation scenarios.

Basic Examples
--------------

Simple Name Generation
^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from naamkaran.generate import generate_names

    # Generate 10 random names
    names = generate_names()
    for name in names:
        print(name)

Gender-Specific Names
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Generate male names
    male_names = generate_names(gender='M', num_names=5)
    print("Male names:", male_names)

    # Generate female names
    female_names = generate_names(gender='F', num_names=5)
    print("Female names:", female_names)

Advanced Examples
-----------------

Names by Starting Letter
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Names starting with vowels
    vowel_names = []
    for vowel in ['A', 'E', 'I', 'O', 'U']:
        names = generate_names(starting_letter=vowel, num_names=2)
        vowel_names.extend(names)

    print("Names starting with vowels:", vowel_names)

Names with Length Constraints
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Short names (4-6 characters)
    short_names = generate_names(max_len=6, num_names=5)
    print("Short names:", short_names)

    # Medium names (7-9 characters)
    medium_names = generate_names(max_len=9, num_names=5)
    print("Medium names:", medium_names)

Temperature Experiments
^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Conservative names (low temperature)
    conservative = generate_names(
        starting_letter='J',
        temperature=0.2,
        num_names=3
    )
    print("Conservative:", conservative)

    # Balanced names (medium temperature)
    balanced = generate_names(
        starting_letter='J',
        temperature=0.8,
        num_names=3
    )
    print("Balanced:", balanced)

    # Creative names (high temperature)
    creative = generate_names(
        starting_letter='J',
        temperature=1.5,
        num_names=3
    )
    print("Creative:", creative)

Practical Use Cases
-------------------

Character Names for Fiction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Fantasy characters
    def generate_fantasy_names():
        return generate_names(
            temperature=1.2,  # More creative
            max_len=8,
            num_names=5
        )

    # Realistic characters
    def generate_realistic_names():
        return generate_names(
            temperature=0.4,  # More conservative
            num_names=5
        )

    fantasy_chars = generate_fantasy_names()
    realistic_chars = generate_realistic_names()

Baby Name Suggestions
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def suggest_baby_names(gender, starting_letter=None, max_suggestions=20):
        """Generate baby name suggestions"""
        return generate_names(
            gender=gender,
            starting_letter=starting_letter,
            temperature=0.6,  # Balanced creativity
            max_len=10,
            num_names=max_suggestions
        )

    # Suggest baby girl names starting with 'S'
    girl_names = suggest_baby_names('F', 'S', 15)
    print("Baby girl names starting with 'S':", girl_names)

Business/Brand Names
^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    def generate_brand_names(letter, count=10):
        """Generate creative brand names"""
        return generate_names(
            starting_letter=letter,
            temperature=1.0,  # Creative but not too wild
            max_len=7,  # Short for branding
            num_names=count
        )

    brand_names = generate_brand_names('T')
    print("Brand name ideas:", brand_names)

Batch Processing
^^^^^^^^^^^^^^^^

.. code-block:: python

    import pandas as pd

    def create_name_dataset(num_names=1000):
        """Create a dataset of generated names"""
        all_names = []

        # Generate names for different starting letters
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            # Male names
            male_names = generate_names(
                starting_letter=letter,
                gender='M',
                num_names=20,
                temperature=0.7
            )
            for name in male_names:
                all_names.append({
                    'name': name,
                    'gender': 'M',
                    'starting_letter': letter,
                    'length': len(name)
                })

            # Female names
            female_names = generate_names(
                starting_letter=letter,
                gender='F',
                num_names=20,
                temperature=0.7
            )
            for name in female_names:
                all_names.append({
                    'name': name,
                    'gender': 'F',
                    'starting_letter': letter,
                    'length': len(name)
                })

        return pd.DataFrame(all_names)

    # Create dataset
    df = create_name_dataset()
    print(f"Generated {len(df)} names")
    print(df.head())

Command Line Examples
---------------------

Here are examples using the command-line interface:

.. code-block:: bash

    # Basic usage
    generate_names -n 5

    # Female names starting with 'M'
    generate_names -s M -g F -n 10

    # Short male names ending with 'n'
    generate_names -e n -g M -m 6 -n 8

    # Creative names with high temperature
    generate_names -t 1.5 -n 5

    # Conservative business names
    generate_names -s T -m 7 -t 0.3 -n 15
