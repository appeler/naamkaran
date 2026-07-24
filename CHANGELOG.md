# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Added the missing `scikit-learn` runtime dependency; the shipped vocab
  pickle requires it to unpickle `CountVectorizer` at load time.

### Changed

- Adopted the `py-canon` fleet standard: CI, docs, and release workflows
  now delegate to `gojiplus/py-canon` reusable workflows; added `pyright`
  and `pydoclint` to the lint/type-check gate.

## [0.2.0]

- Generative LSTM model for names, trained on Florida Voter Registration
  Data, with a CLI and optional Flask/Gradio web front ends.
