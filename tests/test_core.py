# -*- coding: utf-8 -*-

"""Test of vermon.core module."""

import unittest
import re

from vermon.core import _callable_python
from vermon.core import _print_warning
from vermon.core import Vermon

from vermon.exceptions import UnsupportedVersionPattern


class TestVermon(unittest.TestCase):
    """Test class of Vermon package."""

    def setUp(self):
        self.PYTHON_PATTERN = re.compile(r'^python((\d+)(\.\d+)?)?$')

    def test_if_callable_python_function_return_the_python_command(self):
        python = _callable_python()
        match = re.search(self.PYTHON_PATTERN, python)
        self.assertIsNotNone(match, msg=f'python command not found on return: {python}')

    def test_supported_and_unsupported_version_pattern(self):
        supported_version_patterns = ['1.0.0', 'v1.2.3', 'version 3.5.5']
        for v in supported_version_patterns:
            is_supported, __ = Vermon.is_supported_version_pattern(v)
            self.assertTrue(is_supported)

        unsupported_version_patterns = ['', 'v', '1', 'v1', '1.0', 'v2.0', '2..0', 'v2..0..5']
        for v in unsupported_version_patterns:
            with self.assertRaises(UnsupportedVersionPattern, msg=f'This version pattern passed: {v}'):
                Vermon.is_supported_version_pattern(v)
