# Changelog

All notable changes to this project will be documented in this file.

## [0.1.0] - 2025-09-03

### Added
- Modern `pyproject.toml` configuration replacing `setup.py`
- Pre-commit hooks with black, isort, flake8, and mypy
- Comprehensive type hints throughout codebase
- Enhanced Flask API with input validation and error handling
- Additional model tests (`test_020_model.py`)
- Code coverage reporting with pytest-cov
- Support for Python 3.9-3.12

### Changed
- Replaced deprecated `pkg_resources` with `importlib.resources`
- Updated GitHub Actions to test multiple Python versions
- Improved error handling and parameter validation
- Fixed Gradio deprecation warning (`allow_flagging` → `flagging_mode`)
- Enhanced documentation with modern development commands
- Updated dependencies to latest compatible versions

### Fixed
- 35+ code style violations (flake8, black, isort)
- Unused import cleanup
- Trailing whitespace and formatting issues
- Type annotation inconsistencies

### Removed
- Deprecated `pkg_resources` dependency
- Legacy `setup.py` test command configuration

## [0.0.1] - Initial Release
- Basic name generation functionality
- PyTorch-based character-level RNN model
- Gradio and Flask web interfaces
- Command-line interface
