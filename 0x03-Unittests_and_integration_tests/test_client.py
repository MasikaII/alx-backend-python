#!/usr/bin/env python3
"""
Testcases for Classes
"""

import requests
import unittest
from unittest.mock import patch, Mock, PropertyMock, call
from parameterized import parameterized, parameterized_class
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from unittest import expectedFailure, mock


class TestGithubOrgClient(unittest.TestCase):
    """
    A class that tests classes
    of github org client
    """
    @parameterized.expand([
        ("google", {"google": True}),
        ("abc", {"abc": True})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected, get_patch):
        """
        Tests if test org returns correct values
        """
        get_patch.return_value = expected
        y = GithubOrgClient(org)
        self.assertEqual(y.org, expected)
        get_patch.assert_called_once_with('https://api.github.com/orgs/' + org)

    def test_public_repos_url(self):
        """
        Using mocked payload
        """
        expected = 'www.holberton.io'
        payload = {"repos_url": expected}
        to_mock = 'client.GithubOrgClient.org'
        with patch(to_mock, PropertyMock(return_value=payload)):
            cli = GithubOrgClient("y")
            self.assertEqual(cli._public_repos_url, expected)

    parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license"),
        ({"license": {"key": "other_license"}}, "other_license")
    ])

    def test_has_license(self, repo, license, expected):
        """
        Test case
        """
        self.assertEqual(GithubOrgClient.has_license(repo(license), expected))
