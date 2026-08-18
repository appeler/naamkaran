"""Contracts for published name-generation artifacts."""

import hashlib
from pathlib import Path
from unittest.mock import patch

import pytest

from naamkaran._resources import HF_REPO, HF_REVISION, MODEL_MANIFEST, resolve_model


def test_local_override_avoids_the_network(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    model = tmp_path / "naamkaran.pt"
    model.write_bytes(b"weights")
    monkeypatch.setenv("NAAMKARAN_MODEL_DIR", str(tmp_path))
    with patch("huggingface_hub.hf_hub_download") as download:
        assert resolve_model(model.name) == str(model)
    download.assert_not_called()


def test_missing_artifact_uses_exact_pinned_location(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("NAAMKARAN_MODEL_DIR", str(tmp_path))
    downloaded = tmp_path / "downloaded.pt"
    downloaded.write_bytes(b"downloaded weights")
    expected_hash = MODEL_MANIFEST["artifacts"]["naamkaran.pt"]["sha256"]
    with (
        patch(
            "huggingface_hub.hf_hub_download", return_value=str(downloaded)
        ) as download,
        patch("naamkaran._resources._sha256", return_value=expected_hash),
    ):
        assert resolve_model("naamkaran.pt") == str(downloaded)
    download.assert_called_once_with(HF_REPO, "naamkaran.pt", revision=HF_REVISION)


def test_revision_is_an_immutable_commit() -> None:
    assert len(HF_REVISION) == 40
    assert set(HF_REVISION) <= set("0123456789abcdef")


def test_unknown_remote_artifact_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setenv("NAAMKARAN_MODEL_DIR", str(tmp_path))
    with (
        patch("huggingface_hub.hf_hub_download") as download,
        pytest.raises(ValueError, match="Unknown model artifact"),
    ):
        resolve_model("unknown.bin")
    download.assert_not_called()


def test_download_hash_mismatch_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("NAAMKARAN_MODEL_DIR", raising=False)
    downloaded = tmp_path / "naamkaran.pt"
    downloaded.write_bytes(b"corrupt")
    with (
        patch("huggingface_hub.hf_hub_download", return_value=str(downloaded)),
        pytest.raises(RuntimeError, match="integrity check"),
    ):
        resolve_model("naamkaran.pt")


@pytest.mark.live
def test_pinned_revision_contains_every_artifact() -> None:
    from huggingface_hub import hf_hub_download, list_repo_files

    published = set(list_repo_files(HF_REPO, revision=HF_REVISION))
    assert {"naamkaran.pt", "vocabulary.parquet"} <= published
    for filename, metadata in MODEL_MANIFEST["artifacts"].items():
        downloaded = Path(hf_hub_download(HF_REPO, filename, revision=HF_REVISION))
        assert hashlib.sha256(downloaded.read_bytes()).hexdigest() == metadata["sha256"]
        assert downloaded.stat().st_size == metadata["size"]
