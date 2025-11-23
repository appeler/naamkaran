#!/usr/bin/env python

import sys

from .naam import Naamkaran
from .utils import get_args


class GenerateNames(Naamkaran):
    """
    Generates names for the given dataframe.
    """

    MODEL_FN = "models/naamkaran.pt"
    VOCAB_FN = "models/names_vec.joblib"

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
    ) -> list[str]:
        """
        Generates names for the given dataframe.
        """
        return Naamkaran.generate(
            start_letter,
            end_letter,
            how_many,
            max_length,
            gender,
            temperature,
            model_fn or GenerateNames.MODEL_FN,
            vocab_fn or GenerateNames.VOCAB_FN,
        )


generate_names = GenerateNames.generate


def main() -> list[str]:
    """
    Main method to generates names for the given dataframe.
    """

    args = get_args(
        sys.argv[1:],
        "Naamkaran",
        "Generate names for the given dataframe.",
        "Happy naming!",
    )
    names = generate_names(
        args.start_letter,
        args.end_letter,
        args.how_many,
        args.max_length,
        args.gender,
        args.temperature,
    )
    if args.debug:
        print(args)
        print(names)
    return names


if __name__ == "__main__":
    main()
