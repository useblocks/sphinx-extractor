import subprocess
from pathlib import Path

import pytest


@pytest.mark.parametrize("test_app", [{"buildername": "html", "srcdir": "doc_test/test_extract"}], indirect=True)
def test_rst_extract(test_app):
    app = test_app
    app.build()
    html = Path(app.outdir, "index.html").read_text()
    assert html


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/test_extract_negative_invalid_file_path"}],
    indirect=True,
)
def test_rst_extract_negative_invalid_file_path(test_app):
    app = test_app

    srcdir = Path(app.srcdir)
    out_dir = srcdir / "_build"

    out = subprocess.run(["sphinx-build", "-M", "html", srcdir, out_dir], capture_output=True)
    assert out.returncode == 2

    assert "FileNotFoundError: Could not find file" in out.stderr.decode("utf-8")
    assert "test_extract_negative_invalid_file_path/myuml.puml" in out.stderr.decode("utf-8")


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/test_extract_negative_option_end_value_not_found"}],
    indirect=True,
)
def test_rst_extract_negative_option_end_value_not_found(test_app):
    app = test_app

    srcdir = Path(app.srcdir)
    out_dir = srcdir / "_build"

    out = subprocess.run(["sphinx-build", "-M", "html", srcdir, out_dir], capture_output=True)
    assert out.returncode == 1

    assert (
        "sphinx_extractor.directives.extract.ExtractException: "
        "Given value for option end: @somethingNone not found in given file: " in out.stderr.decode("utf-8")
    )
    assert "../utils/mytxt.txt." in out.stderr.decode("utf-8")


@pytest.mark.parametrize(
    "test_app",
    [{"buildername": "html", "srcdir": "doc_test/test_extract_negative_option_start_value_not_found"}],
    indirect=True,
)
def test_rst_extract_negative_option_start_value_not_found(test_app):
    app = test_app

    srcdir = Path(app.srcdir)
    out_dir = srcdir / "_build"

    out = subprocess.run(["sphinx-build", "-M", "html", srcdir, out_dir], capture_output=True)
    assert out.returncode == 1

    assert (
        "sphinx_extractor.directives.extract.ExtractException: "
        "Given value for option start: ### not found in given file: " in out.stderr.decode("utf-8")
    )
    assert "../utils/mytxt.txt." in out.stderr.decode("utf-8")
