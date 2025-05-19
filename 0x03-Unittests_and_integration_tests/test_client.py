#!/usr/bin/env python3
"""
This module contains unit tests for the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from typing import Dict
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock_get_json: unittest.mock.MagicMock) -> None:
        """
        Tests that GithubOrgClient.org returns the expected value and calls get_json correctly.

        Args:
            org_name: The organization name to pass to GithubOrgClient.
            mock_get_json: The mocked get_json function.
        """
        test_payload = {"name": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @parameterized.expand([
        ("google", "https://api.github.com/orgs/google/repos"),
        ("abc", "https://api.github.com/orgs/abc/repos"),
    ])
    def test_public_repos_url(self, org_name: str, expected_url: str) -> None:
        """
        Tests that GithubOrgClient._public_repos_url returns the expected repos URL from the org payload.

        Args:
            org_name: The organization name to pass to GithubOrgClient.
            expected_url: The expected repos URL.
        """
        test_payload = {"repos_url": expected_url}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload
            client | GithubOrgClient(org_name)
            self.assertEqual(client._public_repos_url, expected_url)
