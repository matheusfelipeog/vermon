# -*- coding: utf-8 -*-

"""Test of vermon.core module."""

import unittest
import re

from vermon.core import _callable_python
from vermon.core import _print_warning
from vermon.core import Vermon


class TestVermon(unittest.TestCase):
    """Test class of Vermon package."""

    def setUp(self):
        self.PYTHON_PATTERN = re.compile(r'^python((\d+)(\.\d+)?)?$')

    def test_if_callable_python_function_return_the_python_command(self):
        python = _callable_python()
        match = re.search(self.PYTHON_PATTERN, python)
        self.assertIsNotNone(match, msg=f'python command not found on return: {python}')
