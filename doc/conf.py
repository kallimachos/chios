#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Configuration file for chios documentation."""

import os
import sys
from datetime import datetime

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None

try:
    from sphinxcontrib import spelling
except ImportError as e:
    print(e)
    spelling = None

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../chios/"))

try:
    from chios import __version__
except ImportError:
    print("Cannot load version.")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
]

if spelling is not None:
    extensions.append("sphinxcontrib.spelling")

source_suffix = ".rst"
master_doc = "index"
project = "chios"
copyright = f"{datetime.now().year}, Brian Moss"
author = "Brian Moss"
version = __version__
language = None
exclude_patterns = ["_build", "README.rst"]
pygments_style = "sphinx"
if sphinx_rtd_theme:
    html_theme = "sphinx_rtd_theme"
else:
    html_theme = "default"
html_logo = "_static/chios.png"
html_favicon = "_static/chios.ico"
html_static_path = ["_static"]
html_css_files = ["theme_overrides.css"]
html_use_smartypants = False
htmlhelp_basename = "doc"
html_permalinks = True
html_permalinks_icon = "#"
