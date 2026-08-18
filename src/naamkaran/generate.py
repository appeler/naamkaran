"""Command-line entry point for generating names."""

import sys

from .naam import Naamkaran
from .utils import get_args


class GenerateNames(Naamkaran):
    """Generate synthetic name-like strings from the published model."""

    MODEL_FN = "models/naamkaran.pt"
    VOCAB_FN = "models/vocabulary.parquet"

    @staticmethod
    def generate(
        start_letter: str,
        end_letter: str | None = None,
        how_many: int = 1,
        max_length: int = 5,
        gender: str = "M",
        temperature: float = 0.5,
        model_fn: str = "",
        vocab_fn: str = "",
        max_attempts: int | None = None,
    ) -> list[str]:
        """Generate name-like strings from the published model artifacts."""
        return Naamkaran.generate(
            start_letter,
            end_letter,
            how_many,
            max_length,
            gender,
            temperature,
            model_fn or GenerateNames.MODEL_FN,
            vocab_fn or GenerateNames.VOCAB_FN,
            max_attempts,
        )


generate_names = GenerateNames.generate


def main(argv: list[str] | None = None) -> int:
    """Run the command-line interface and print one generated string per line."""
    args = get_args(
        sys.argv[1:] if argv is None else argv,
        "Naamkaran",
        "Generate synthetic name-like strings from the published model.",
        "Happy naming!",
    )
    names = generate_names(
        args.start_letter,
        args.end_letter,
        args.how_many,
        args.max_length,
        args.gender,
        args.temperature,
        max_attempts=args.max_attempts,
    )
    sys.stdout.write("\n".join(names) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
