"""Resolve immutable name-generation artifacts."""

from __future__ import annotations

import os
from pathlib import Path

HF_REPO = "gojiberries/naamkaran"
HF_REVISION = "eaf48b954ae49328de09f8dc4984da9e6f113cbf"
MODEL_DIR_ENV = "NAAMKARAN_MODEL_DIR"


def resolve_model(filename: str) -> str:
    """Return a local path for a pinned model artifact."""
    override = os.environ.get(MODEL_DIR_ENV)
    if override:
        candidate = Path(override) / filename
        if candidate.is_file():
            return str(candidate)

    from huggingface_hub import hf_hub_download

    return hf_hub_download(HF_REPO, filename, revision=HF_REVISION)
