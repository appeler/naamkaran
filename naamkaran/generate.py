#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pandas as pd

from .naam import Naamkaran
from .utils import get_args


class GenerateNames(Naamkaran):
    """
    Generates names for the given dataframe.
    """

    MODEL_FN = "models/naamkaran.pt"
    VOCAB_FN = "models/names_vec.joblib"

    @classmethod
    def generate(cls, start_letter, end_letter=None, how_many=1,
                 max_length=5, gender="M", temperature=0.5) -> pd.DataFrame:
        """
        Generates names for the given dataframe.
        """
        return super().generate(
            start_letter, end_letter, how_many, max_length, gender, temperature,
            cls.MODEL_FN, cls.VOCAB_FN
        )


generate_names = GenerateNames.generate


def main() -> None:
    """
    Main method to generates names for the given dataframe.
    """

    args = get_args(sys.argv[1:], "Naamkaran", "Generate names for the given dataframe.", "Happy naming!")
    names = generate_names(args.start_letter, args.end_letter, args.how_many,
                           args.max_length, args.gender, args.temperature)
    if args.debug:
        print(args)
        print(names)
    return names


if __name__ == "__main__":
    sys.exit(main())
