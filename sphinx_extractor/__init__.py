"""A Sphinx extension to extract rst code from text-based files."""
from sphinx_extractor.directives.extract import ExtractDirective

VERSION = "0.1.0"


def setup(app):
    app.add_directive("extract", ExtractDirective)

    return {
        "version": VERSION,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
