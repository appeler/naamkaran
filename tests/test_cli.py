"""Command-line interface contracts."""

from unittest.mock import patch

from naamkaran.generate import main


def test_main_prints_names_and_returns_success(capsys) -> None:
    """The installed console script writes output and returns a zero status."""
    with patch("naamkaran.generate.generate_names", return_value=["Ari", "Avi"]):
        status = main(["--start_letter", "A", "--how_many", "2"])

    assert status == 0
    assert capsys.readouterr().out == "Ari\nAvi\n"
