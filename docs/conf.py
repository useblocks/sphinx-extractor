# Rst-Extractor documentation build configuration file

# -- General configuration ------------------------------------------------

import os
import sys

sys.path.append(os.path.abspath("../sphinx_extractor"))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_extractor"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
root_doc = "index"

# General information about the project.
project = "Rst-Extractor"
copyright = "2022, team useblocks"
author = "team useblocks"

version = "0.1"

language = "en"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
