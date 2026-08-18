"""Core name-generation logic backed by the trained LSTM model."""

from __future__ import annotations

import math

import pyarrow.parquet as pq
import torch

from ._resources import resolve_model
from .model import NameGenerator


class Naamkaran:
    """Generates names for the given start_letter, end_letter."""

    ATTEMPTS_PER_REQUESTED_NAME = 1_000

    @staticmethod
    def _validate_request(
        start_letter: str,
        end_letter: str | None,
        how_many: int,
        max_length: int,
        gender: str,
        temperature: float,
        max_attempts: int | None,
    ) -> int:
        """Validate generation controls and return a finite attempt budget."""
        if not isinstance(start_letter, str) or len(start_letter) != 1:
            raise ValueError("start_letter must be exactly one character")
        if end_letter is not None and (
            not isinstance(end_letter, str) or len(end_letter) != 1
        ):
            raise ValueError("end_letter must be exactly one character or None")
        if not isinstance(how_many, int) or isinstance(how_many, bool) or how_many < 1:
            raise ValueError("how_many must be a positive integer")
        if (
            not isinstance(max_length, int)
            or isinstance(max_length, bool)
            or max_length < 1
        ):
            raise ValueError("max_length must be a positive integer")
        if gender not in {"F", "M"}:
            raise ValueError("gender must be 'F' or 'M'")
        if (
            not isinstance(temperature, (int, float))
            or isinstance(temperature, bool)
            or not math.isfinite(temperature)
            or temperature <= 0
        ):
            raise ValueError("temperature must be finite and greater than zero")
        if max_attempts is None:
            return how_many * Naamkaran.ATTEMPTS_PER_REQUESTED_NAME
        if (
            not isinstance(max_attempts, int)
            or isinstance(max_attempts, bool)
            or max_attempts < how_many
        ):
            raise ValueError("max_attempts must be an integer at least how_many")
        return max_attempts

    @staticmethod
    def _is_stop_token(token_index: int, vocabulary_size: int) -> bool:
        """Return whether a sampled index is a boundary or reserved token."""
        return token_index == 0 or token_index >= vocabulary_size

    @staticmethod
    def generate(
        start_letter: str,
        end_letter: str | None,
        how_many: int,
        max_length: int,
        gender: str,
        temperature: float,
        model_fn: str,
        vocab_fn: str,
        max_attempts: int | None = None,
    ) -> list[str]:
        """Generate name-like strings with bounded rejection sampling.

        Args:
            start_letter: Required first character.
            end_letter: Optional required final character.
            how_many: Number of strings to return.
            max_length: Maximum characters per string.
            gender: Binary conditioning value from the trained model (``F`` or
                ``M``).
            temperature: Positive softmax sampling temperature.
            model_fn: Model artifact name or local override filename.
            vocab_fn: Vocabulary artifact name or local override filename.
            max_attempts: Maximum candidates to sample before failing. Defaults
                to 1,000 attempts per requested string.

        Returns:
            Generated name-like strings.

        Raises:
            ValueError: If a generation control is invalid or a requested
                character is outside the model vocabulary.
            RuntimeError: If the requested number of strings cannot be produced
                within ``max_attempts``.
        """
        attempt_budget = Naamkaran._validate_request(
            start_letter,
            end_letter,
            how_many,
            max_length,
            gender,
            temperature,
            max_attempts,
        )
        model_path = resolve_model(model_fn.removeprefix("models/"))
        vocab_path = resolve_model(vocab_fn.removeprefix("models/"))

        vocab = pq.read_table(vocab_path, columns=["token"])["token"].to_pylist()
        n_letters = len(vocab)
        all_letters = "".join(vocab)
        if start_letter not in all_letters:
            raise ValueError("start_letter is outside the model vocabulary")
        if end_letter is not None and end_letter not in all_letters:
            raise ValueError("end_letter is outside the model vocabulary")
        # Hyperparameters
        hidden_size = 100
        n_layers = 1
        gender_size = 2

        vocab_size = n_letters + 2
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        # Initialize the model
        model = NameGenerator(
            vocab_size, gender_size, hidden_size, vocab_size, n_layers
        )
        model.load_state_dict(
            torch.load(model_path, map_location=device, weights_only=True)  # nosec B614
        )
        model.to(device)

        # set the model to evaluation mode
        model.eval()
        generated_names = []

        gender_to_idx = {"F": 0, "M": 1}
        for _ in range(attempt_budget):
            # Convert start_letter to a tensor
            input_tensor = torch.full(
                (1,), all_letters.find(start_letter), dtype=torch.long
            ).to(device)

            # Initialize hidden state
            hidden = model.init_hidden(1, device)

            # Convert gender to a tensor
            gender_tensor = (
                torch.tensor(gender_to_idx[gender], dtype=torch.long)
                .unsqueeze(0)
                .to(device)
            )

            # Initialize the generated name with the start letter
            generated_name = start_letter
            # Repeatedly predict the next character
            for _ in range(max_length - 1):
                # Forward pass
                with torch.no_grad():
                    output, hidden = model(
                        input_tensor.unsqueeze(0), gender_tensor, hidden
                    )
                    output_dist = torch.softmax(output[0] / temperature, dim=-1)
                    top_idx = int(torch.multinomial(output_dist, 1).item())

                # Check if the index is out-of-bounds, which might signal the end
                if Naamkaran._is_stop_token(top_idx, n_letters):
                    break

                # Append the predicted letter to the generated name
                next_letter = all_letters[top_idx]
                generated_name += next_letter

                # Update the input tensor for the next iteration
                input_tensor = torch.tensor([top_idx], dtype=torch.long).to(device)

            matches_requested_end = (
                end_letter is None or generated_name[-1] == end_letter
            )
            if matches_requested_end and generated_name not in generated_names:
                generated_names.append(generated_name)
                if len(generated_names) == how_many:
                    return generated_names

        raise RuntimeError(
            f"Generated {len(generated_names)} of {how_many} requested strings "
            f"within {attempt_budget} attempts"
        )
