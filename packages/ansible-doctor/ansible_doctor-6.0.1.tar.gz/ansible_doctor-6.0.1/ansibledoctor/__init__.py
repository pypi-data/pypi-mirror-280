"""Provide version information."""

__version__ = "6.0.1"

import sys

try:
    import ansible  # noqa
except ImportError:
    sys.exit("ERROR: Python requirements are missing: 'ansible-core' not found.")
