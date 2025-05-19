#!/usr/bin/env python3
"""
This module contains unit tests for the utils module.
"""

import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[str, ...], expected: Union[Dict, int]) -> None:
        """
        Tests that access_nested_map returns the expected value for given inputs.

        Args:
            nested_map: The nested dictionary to access.
            path: A tuple of keys representing the path to the value.
            expected: The expected value at the specified path.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str, ...], expected_key: str) -> None:
        """
        Tests that access_nested_map raises a KeyError with the expected key for invalid inputs.

        Args:
            nested_map: The nested dictionary to access.
            path: A tuple of keys representing the path to the value.
            expected_key: The key expected in the KeyError message.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{expected_key}'")
