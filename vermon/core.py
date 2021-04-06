# -*- coding: utf-8 -*-

"""
vermon.core
-----------

This module contains the core implementation of vermon package.
"""

__all__ = [
    'print_warning',
    'Vermon'
]

from vermon.__about__ import __version__
from vermon.__about__ import __author__
from vermon.__about__ import __email__
from vermon.__about__ import __author_github__
from vermon.__about__ import __project_github__

import sys
import os
import re

import requests

from vermon.exceptions import UnsupportedVersionPattern


PYPI = 'https://pypi.org/pypi/{package}/json'

VERSION_PATTERN = re.compile(r'[0-9]+\.[0-9]+\.[0-9]+')


def _callable_python() -> str:
    """Returns the string that is used to run Python in the terminal.
    
    This is necessary for the warning to indicate the correct python executor,
    regardless of the python version, of OS and virtual environment where 
    the vermon module is being used.
    """

    python = os.path.basename(sys.executable)

    if python.endswith('.exe'):
        python = python.rstrip('.exe')
    
    return python


def print_warning(package: str, current_version: str, latest_version: str):
    """Print a warning if of package has a newer version."""

    warning_message = (
        'You are using an old version of the {package} package (v{current_version}), '
        'a new version has been released (v{latest_version}).\n'
        'Please run: {python} -m pip install {package} --upgrade'
    ).format(
        package=package,
        current_version=current_version,
        latest_version=latest_version,
        python=_callable_python()
    )

    print(warning_message)


class Vermon(object):
    """Check if package has a newer version."""

    def __init__(self, package: str, current_version: str):
        self.package = package
        self.current_version = self.get_only_version(current_version)
        self.latest_version = self.get_only_version(self.get_latest_version())

    def __repr__(self):
        return (
            'Vermon('
            f'package=<{self.package}>, '
            f'current_version=<{self.current_version}>, '
            f'latest_version=<{self.latest_version}>)'
        )
    
    def __str__(self):
        return f'Vermon(package={self.package}, current_version={self.current_version})'

    @staticmethod
    def is_supported_version_pattern(version: str) -> tuple:
        """Check if the version pattern is in a supported format."""

        match = VERSION_PATTERN.search(version)

        if not match:
            raise UnsupportedVersionPattern(f'This version pattern ({version}) is not supported.')
        
        return True, match.group()

    @staticmethod
    def get_only_version(version: str) -> str:
        """Get only version if it exists."""

        is_supported, version = Vermon.is_supported_version_pattern(version)

        if is_supported:
            return str(version)

    @staticmethod
    def version_to_tuple(version: str, separator='.') -> tuple:
        """Convert version to tuple. 
        
        Example
        -------
        '1.4.3' version to tuple:
        
            >>> from vermon import Vermon
            >>> Vermon.version_to_tuple('1.4.3')
            (1, 4, 3).
        """

        major, minor, patch = map(int, version.split(separator))

        return (major, minor, patch)

    def build_endpoint(self) -> str:
        """Build endpoint of pypi API with package name."""

        return PYPI.format(package=self.package)

    def get_latest_version(self) -> str:
        """Get latest version in pypi platform."""

        endpoint = self.build_endpoint()
        response = requests.get(
            endpoint,
            headers={
                'User-Agent': f'Vermon v{__version__} <https://github.com/matheusfelipeog/vermon>',
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
        )
        
        if response.ok:
            return response.json()['info']['version']

    def is_newer_version_available(self) -> bool:
        """Check if latest version is greater than the current version."""

        current_version = self.version_to_tuple(self.current_version)
        latest_version = self.version_to_tuple(self.latest_version)

        if latest_version > current_version:
            return True
        
        return False

    @staticmethod
    def run(package: str, current_version: str):
        """Run vermon without instantiating an object."""

        vermon = Vermon(package, current_version)
        
        is_newer_version = vermon.is_newer_version_available()

        if is_newer_version:
            print_warning(
                package=vermon.package,
                current_version=vermon.current_version,
                latest_version=vermon.latest_version
            )
