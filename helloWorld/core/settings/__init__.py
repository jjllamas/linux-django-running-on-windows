# -*- coding: utf-8 -*-
"""
Settings configuration for a proper development:

settings
+-- __init__.py
+-- defaults.py
+-- local.py

Your settings should be defined in local.py and in that file
add the following:

from default import *

Do NOT set up your local settings under version control

"""
class LocalSettingsException(Exception):
    """Base class for exceptions in this module."""
    pass

try:
    from local import *
except ImportError as e:
    raise LocalSettingsException( __doc__)