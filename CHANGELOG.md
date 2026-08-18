# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.0] - 2026-08-17

### Changed

- Store model weights and the typed Parquet vocabulary on Hugging Face at an
  immutable revision instead of shipping weights and a version-sensitive
  scikit-learn pickle in the wheel.
- Verify downloaded artifact hashes against a packaged model manifest.
- Adopt the py-canon project structure, uv_build backend, quality checks, and
  reusable release workflows.
- Move the import package to the standard `src` layout.
- Bound rejection sampling and validate generation controls so impossible
  requests fail instead of hanging indefinitely.

### Fixed

- Treat both reserved model output indices as stop tokens instead of indexing
  past the end of the vocabulary.
- Make the console command print generated strings and exit successfully.

## [0.2.0]

- Generative LSTM model for names, trained on Florida Voter Registration
  Data, with a CLI and optional Flask/Gradio web front ends.
