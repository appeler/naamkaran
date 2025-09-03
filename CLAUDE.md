# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Naamkaran is a generative model for names built with PyTorch. It uses a character-level RNN (LSTM) trained on Florida Voter Registration Data to generate names based on starting letter, ending letter, gender, and other parameters.

## Key Architecture

The project follows a simple Python package structure:

- `naamkaran/naam.py`: Core `Naamkaran` class containing the name generation logic using PyTorch model
- `naamkaran/model.py`: `NameGenerator` neural network model (LSTM with embeddings for characters and gender)
- `naamkaran/generate.py`: `GenerateNames` class that wraps the core functionality and provides the main `generate_names` function
- `naamkaran/utils.py`: Command-line argument parsing utilities
- `naamkaran/models/`: Contains pre-trained model files (`naamkaran.pt`, `names_vec.joblib`)
- `gradio_app.py`: Gradio web interface for interactive name generation
- `flask/flask_api.py`: Flask API wrapper for the name generation functionality

The model loads pre-trained weights from `models/naamkaran.pt` and vocabulary from `models/names_vec.joblib` using joblib.

## Development Commands

### Setup and Installation
```bash
# Install package in development mode with all dependencies
pip install -e ".[dev,test]"

# Install pre-commit hooks
pre-commit install
```

### Testing
```bash
# Run all tests with coverage
pytest --cov=naamkaran

# Run specific test file
pytest naamkaran/tests/test_010_gen_names.py

# Run tests with verbose output
pytest -v
```

### Code Quality
```bash
# Format code with black
black naamkaran/

# Sort imports
isort naamkaran/

# Lint with flake8
flake8 naamkaran/

# Type check with mypy
mypy naamkaran/

# Run pre-commit on all files
pre-commit run --all-files
```

### Running Applications
```bash
# Run Gradio web interface
python3 gradio_app.py

# Run Flask API
python3 flask/flask_api.py

# Command-line usage (requires package installation)
generate_names -s A -e e -n 5 -m 6 -g F -t 0.7
```

### Documentation
```bash
# Build documentation with Sphinx
cd docs && make html
```

## Dependencies and Environment

- **Python**: 3.6-3.10 (setup.py specifies compatibility)
- **Core ML**: PyTorch 2.6.0, scikit-learn 1.5.1
- **Data**: pandas 2.0.3, joblib 1.3.2
- **Web Apps**: Gradio (for gradio_app.py), Flask (for flask/flask_api.py)
- **Testing**: pytest 7.4.0, unittest (built-in)

The project includes a virtual environment (`venv/`) that may not be properly configured on the current system.

## Important Notes

- **Scikit-learn version warning**: The pre-trained model was created with scikit-learn 1.2.2, but current version is 1.5.1+. This may cause warnings but functionality is preserved.
- **Model files**: Large binary assets (`models/naamkaran.pt`, `models/names_vec.joblib`) are required for the package to function
- **Development**: Use `pyproject.toml` for modern packaging (replaces `setup.py`)
- **Code quality**: Pre-commit hooks are configured for automatic formatting with black, isort, flake8, and mypy
