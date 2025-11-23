#!/usr/bin/env python

"""
test_020_model
Tests for the NameGenerator model
"""

import unittest

import torch

from naamkaran.model import NameGenerator


class TestNameGenerator(unittest.TestCase):
    """
    Test NameGenerator model.
    """

    def setUp(self) -> None:
        self.input_size = 57
        self.gender_size = 2
        self.hidden_size = 100
        self.output_size = 57
        self.n_layers = 1
        self.batch_size = 1
        self.seq_len = 5
        self.model = NameGenerator(
            self.input_size,
            self.gender_size,
            self.hidden_size,
            self.output_size,
            self.n_layers,
        )

    def test_model_initialization(self) -> None:
        """Test model initializes correctly."""
        self.assertEqual(self.model.hidden_size, self.hidden_size)
        self.assertEqual(self.model.n_layers, self.n_layers)

    def test_forward_pass(self) -> None:
        """Test forward pass produces correct output shapes."""
        input_seq = torch.randint(0, self.input_size, (self.batch_size, self.seq_len))
        gender = torch.randint(0, self.gender_size, (self.batch_size,))
        hidden = self.model.init_hidden(self.batch_size, "cpu")

        output, hidden_out = self.model(input_seq, gender, hidden)

        self.assertEqual(
            output.shape, (self.batch_size, self.seq_len, self.output_size)
        )
        self.assertEqual(len(hidden_out), 2)  # LSTM returns (h_n, c_n)

    def test_init_hidden(self) -> None:
        """Test hidden state initialization."""
        hidden = self.model.init_hidden(self.batch_size, "cpu")
        h_0, c_0 = hidden

        expected_shape = (self.n_layers, self.batch_size, self.hidden_size)
        self.assertEqual(h_0.shape, expected_shape)
        self.assertEqual(c_0.shape, expected_shape)


if __name__ == "__main__":
    unittest.main()
