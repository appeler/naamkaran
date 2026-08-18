"""Validation and token-boundary contracts for name generation."""

from __future__ import annotations

import pytest

from naamkaran.naam import Naamkaran


@pytest.mark.parametrize(
    "overrides",
    [
        {"start_letter": ""},
        {"start_letter": "ab"},
        {"end_letter": "ab"},
        {"how_many": 0},
        {"how_many": True},
        {"max_length": 0},
        {"gender": "X"},
        {"temperature": 0},
        {"temperature": True},
        {"temperature": float("inf")},
        {"max_attempts": 0},
    ],
)
def test_invalid_generation_controls_fail_before_loading_models(
    overrides: dict[str, object],
) -> None:
    """Invalid requests fail deterministically without touching model assets."""
    arguments = {
        "start_letter": "a",
        "end_letter": None,
        "how_many": 1,
        "max_length": 5,
        "gender": "F",
        "temperature": 0.5,
        "max_attempts": None,
        **overrides,
    }
    with pytest.raises(ValueError, match="must be"):
        Naamkaran._validate_request(**arguments)


def test_default_attempt_budget_scales_with_requested_count() -> None:
    """The rejection-sampling budget is explicit and proportional."""
    budget = Naamkaran._validate_request("a", None, 3, 5, "F", 0.5, None)
    assert budget == 3 * Naamkaran.ATTEMPTS_PER_REQUESTED_NAME


def test_every_non_vocabulary_model_index_is_a_stop_token() -> None:
    """Both reserved model outputs stop generation instead of indexing past tokens."""
    vocabulary_size = 55
    assert Naamkaran._is_stop_token(0, vocabulary_size)
    assert Naamkaran._is_stop_token(55, vocabulary_size)
    assert Naamkaran._is_stop_token(56, vocabulary_size)
    assert not Naamkaran._is_stop_token(54, vocabulary_size)
