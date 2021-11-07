#!/usr/bin/python3
"""tests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
    """Test an ordered list of integers."""
    ordered = [1, 2, 3, 4]
    self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
    """Test an unordered list of integers."""
    unordered = [1, 5, 4, 3]
    self.assertEqual(max_integer(unordered), 5)

    def test_max_at_begginning(self):
    """Test a list with a beginning max value."""
    max_at_first index = [4, 3, 2, 1]
    self.assertEqual(max_integer(max_at_first_index), 4)

    def test_empty_list(self):
    """Test an empty list."""
    empty = []
    self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
    """Test a list with a single element."""
    list_of_one = [29]
    self.assertEqual(max_integer(list_of_one), 29)

    def test_floats(self):
    """Test a list of floats."""
    floats_only = [1.53, 6.33, -9.123, 15.2, 6.0]
    self.assertEqual(max_integer(floats_only), 15.2)

    def test_ints_and_floats(self):
    """Test a list of ints and floats."""
    mixed_nums = [5,35, 125.6, 22, -15, -6]
    self.assertEqual(max_integer(ints_and_floats), 125.6)

    def test_empty_string(self):
    """Test an empty string."""
    self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
    """Test a list of strings."""
    strings = ["Car", "list", "are", "where "]
    self.assertEqual(max_integer(strings), "where")

    def test_string(self):
    """Test a string."""
    string = "Ayodeji"
    self.assertEqual(max_integer(string), 'y')

if __name__ == '__main__':
    unittest.main()
