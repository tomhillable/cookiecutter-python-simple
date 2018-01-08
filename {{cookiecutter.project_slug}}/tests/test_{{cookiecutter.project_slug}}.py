#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from {{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}


class Test{{ cookiecutter.project_slug|title }}(unittest.TestCase):
    """Tests for `{{ cookiecutter.project_slug }}` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_function_returns_true(self):
        """Test function returns true."""
        self.assertTrue({{cookiecutter.project_slug}}.function())


if __name__ == '__main__':
    unittest.main()
