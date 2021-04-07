# -*- coding: utf-8 -*-

"""
Vermon Package
--------------

This package is used to check for a newer version of 
a package and notify the user about it.
"""

from vermon.__about__ import __version__
from vermon.__about__ import __author__
from vermon.__about__ import __email__
from vermon.__about__ import __author_github__
from vermon.__about__ import __project_github__

from vermon.core import Vermon

from vermon.exceptions import UnsupportedVersionPattern
from vermon.exceptions import PackageNotFound
from vermon.exceptions import PackageNotFoundOnPypi
