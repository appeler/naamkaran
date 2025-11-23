"""
To process arguments from the command line.
"""

import argparse


def get_args(
    argv: list[str], prog: str, description: str, epilog: str
) -> argparse.Namespace:
    """
    Returns arguments from the command line.
    """
    parser = argparse.ArgumentParser(
        prog=prog,
        description=description,
        epilog=epilog,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-s",
        "--start_letter",
        type=str,
        default="a",
        help="The starting letter of the name.",
    )
    parser.add_argument(
        "-e",
        "--end_letter",
        type=str,
        default=None,
        help="The ending letter of the name.",
    )
    parser.add_argument(
        "-n",
        "--how_many",
        type=int,
        default=1,
        help="How many names to generate.",
    )
    parser.add_argument(
        "-m",
        "--max_length",
        type=int,
        default=5,
        help="Maximum length of the name.",
    )
    parser.add_argument(
        "-g",
        "--gender",
        type=str,
        default="M",
        help="Gender of the name.",
    )
    parser.add_argument(
        "-t",
        "--temperature",
        type=float,
        default=0.5,
        help="Temperature for the softmax function.",
    )

    args = parser.parse_args(argv)
    return args
