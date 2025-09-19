Contributing
============

We welcome contributions to naamkaran! This document provides guidelines for contributing to the project.

Development Setup
-----------------

1. **Fork and Clone**

   Fork the repository on GitHub and clone your fork:

   .. code-block:: bash

       git clone https://github.com/YOUR_USERNAME/naamkaran.git
       cd naamkaran

2. **Create Virtual Environment**

   .. code-block:: bash

       python -m venv venv
       source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. **Install Development Dependencies**

   .. code-block:: bash

       pip install -e ".[dev,test]"

4. **Install Pre-commit Hooks**

   .. code-block:: bash

       pre-commit install

Code Style
----------

We use several tools to maintain code quality:

* **Black** for code formatting
* **isort** for import sorting
* **flake8** for linting
* **mypy** for type checking

Run these tools before committing:

.. code-block:: bash

    # Format code
    black naamkaran/

    # Sort imports
    isort naamkaran/

    # Lint code
    flake8 naamkaran/

    # Type check
    mypy naamkaran/

Or run all at once:

.. code-block:: bash

    pre-commit run --all-files

Testing
-------

We use pytest for testing. Run tests with:

.. code-block:: bash

    # Run all tests
    pytest

    # Run with coverage
    pytest --cov=naamkaran

    # Run specific test file
    pytest naamkaran/tests/test_010_gen_names.py

Write tests for new features and ensure existing tests pass.

Documentation
-------------

Documentation is built with Sphinx. To build docs locally:

.. code-block:: bash

    cd docs
    make html

The built documentation will be in ``docs/build/html/``.

For new features, please:

* Add docstrings to functions and classes
* Update relevant documentation files
* Add examples if appropriate

Pull Request Process
--------------------

1. **Create a Branch**

   Create a new branch for your feature or bugfix:

   .. code-block:: bash

       git checkout -b feature/your-feature-name

2. **Make Changes**

   * Write clear, focused commits
   * Follow the code style guidelines
   * Add tests for new functionality
   * Update documentation as needed

3. **Test Your Changes**

   .. code-block:: bash

       # Run tests
       pytest --cov=naamkaran

       # Run linting
       pre-commit run --all-files

       # Test documentation build
       cd docs && make html

4. **Submit Pull Request**

   * Push your branch to GitHub
   * Create a pull request with a clear description
   * Reference any related issues

Pull Request Guidelines
-----------------------

* **Title**: Use a clear, descriptive title
* **Description**: Explain what changes you made and why
* **Tests**: Include tests for new features
* **Documentation**: Update docs for user-facing changes
* **Backwards Compatibility**: Avoid breaking changes when possible

Example PR description:

.. code-block:: text

    ## Summary
    Add support for generating names with custom length ranges

    ## Changes
    - Added min_len parameter to generate_names function
    - Updated CLI to accept --min-len argument
    - Added tests for length range validation
    - Updated documentation with examples

    ## Breaking Changes
    None

    ## Testing
    - Added test_length_range_validation
    - All existing tests pass

Reporting Issues
----------------

When reporting bugs or requesting features:

1. **Search existing issues** first
2. **Use issue templates** when available
3. **Provide clear reproduction steps** for bugs
4. **Include environment details** (Python version, OS, etc.)

Types of Contributions
----------------------

We welcome various types of contributions:

**Bug Fixes**
  Fix issues in existing functionality

**New Features**
  Add new capabilities to the library

**Documentation**
  Improve or expand documentation

**Tests**
  Add or improve test coverage

**Performance**
  Optimize existing code

**Examples**
  Add usage examples and tutorials

Release Process
---------------

Releases are handled by maintainers:

1. Update version in ``pyproject.toml``
2. Update ``CHANGELOG.md``
3. Create release tag
4. GitHub Actions automatically publishes to PyPI

Community Guidelines
--------------------

* Be respectful and inclusive
* Help others learn and grow
* Focus on constructive feedback
* Follow the code of conduct

Getting Help
------------

If you need help:

* Check the documentation
* Search existing issues
* Ask questions in discussions
* Reach out to maintainers

Thank you for contributing to naamkaran!
