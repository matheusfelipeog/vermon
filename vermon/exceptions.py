# -*- coding: utf-8 -*-

"""All exceptions used in vermon package."""


class UnsupportedVersionPattern(Exception):
    """Used to raise a exception for the unsupported version pattern."""


class PackageNotFound(Exception):
    """Used to raise a exception when package not found on platform."""


class PackageNotFoundOnPypi(PackageNotFound):
    """Used to raise a exception when package not found on Pypi."""
