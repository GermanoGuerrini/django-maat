"""
Application that optimizes large ordered data set retrieving when using MySql.
"""

VERSION = (0, 4)


def get_version():
    """Returns the version as a string."""
    return '.'.join(map(str, VERSION))