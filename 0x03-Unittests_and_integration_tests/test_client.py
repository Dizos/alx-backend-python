#!/usr/bin/env python3
"""
This module contains unit tests for the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized, parameterized_class
from typing import Dict, List
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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
            client = GithubOrgClient(org_name)
            self.assertEqual(client._public_repos_url, expected_url)

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: unittest.mock.MagicMock) -> None:
        """
        Tests that GithubOrgClient.public_repos returns the expected list of repos and mocks are called once.

        Args:
            mock_get_json: The mocked get_json function.
        """
        test_url = "https://api.github.com/orgs/test/repos"
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        expected_repos = ["repo1", "repo2"]
        mock_get_json.return_value = test_payload
        with patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock) as mock_url:
            mock_url.return_value = test_url
            client = GithubOrgClient("test")
            self.assertEqual(client.public_repos(), expected_repos)
            mock_get_json.assert_called_once_with(test_url)
            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool) -> None:
        """
        Tests that GithubOrgClient.has_license returns whether the repo has the specified license.

        Args:
            repo: The repository dictionary containing license information.
            license_key: The license key to check.
            expected: The expected boolean result.
        """
        client = GithubOrgClient("test")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test case for the GithubOrgClient class.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """
        Sets up the class by mocking requests.get to return fixture payloads for expected URLs.
        """
        def get_side_effect(url: str) -> Mock:
            mock_response = Mock()
            if url == "https://api.github.com/orgs/test":
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_response.json.return_value = cls.repos_payload
            return mock_response

        cls.get_patcher = patch("requests.get", side_effect=get_side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Tears down the class by stopping the requests.get patcher.
        """
        cls.get_patcher.stop()
