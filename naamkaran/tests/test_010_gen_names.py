#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_010_gen_names
"""

import unittest
from naamkaran.generate import generate_names


class TestGenerateNames(unittest.TestCase):
    """
    Test generate_names method.
    """

    def setUp(self) -> None:
        self.start_letter = "a"
        self.end_letter = "e"
        self.how_many = 1
        self.max_length = 5
        self.gender = "F"
        self.temperature = 0.5

    def tearDown(self) -> None:
        pass

    def test_generate(self) -> None:
        """
        Test generate method.
        """
        names = generate_names(self.start_letter, self.end_letter, self.how_many,
                               self.max_length, self.gender, self.temperature)
        self.assertEqual(len(names), self.how_many)
        self.assertEqual(names[0], self.start_letter)
        self.assertEqual(names[-1], self.end_letter)
        self.assertEqual(len(names[0]), self.max_length)
