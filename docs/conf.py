# Sphinx-Extractor documentation build configuration file

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

# The root toctree document.
root_doc = "index"

# General information about the project.
project = "Sphinx-Extractor"
copyright = "2022, team useblocks"
author = "team useblocks"

version = "0.1.0"

language = "en"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "alabaster"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "github_user": "useblocks",
    "github_repo": "sphinx-extractor",
    "github_banner": True,
}

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        root_doc,
        "sphinx-extractor",
        "sphinx-extractor Documentation",
        author,
        "sphinx-extractor",
        "One line description of project.",
        "Miscellaneous",
    ),
]
