#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from typing import List, Optional

from .naam import Naamkaran
from .utils import get_args


class GenerateNames(Naamkaran):
    """
    Generates names for the given dataframe.
    """

    MODEL_FN = "models/naamkaran.pt"
    VOCAB_FN = "models/names_vec.joblib"

    @classmethod
    def generate(
        cls,
        start_letter: str,
        end_letter: Optional[str] = None,
        how_many: int = 1,
        max_length: int = 5,
        gender: str = "M",
        temperature: float = 0.5,
    ) -> List[str]:
        """
        Generates names for the given dataframe.
        """
        return super().generate(
            start_letter,
            end_letter,
            how_many,
            max_length,
            gender,
            temperature,
            cls.MODEL_FN,
            cls.VOCAB_FN,
        )


generate_names = GenerateNames.generate


def main() -> List[str]:
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
    sys.exit(main())
