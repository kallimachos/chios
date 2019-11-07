#!/bin/python3
# coding: utf-8
"""Remotecode test file."""

from sphinx_testing import TestApp as MakeApp  # rename to prevent warning

htmlfile = "index.html"
highlight = '<div class="highlight">'
sourcecode = '<span class="s">Wile E. Coyote</span>'


def test_remotecode():
    """Test remotecode."""
    app = MakeApp(srcdir="tests/sample", copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    html = (app.outdir / htmlfile).read_text()
    assert highlight in html
    assert sourcecode in html


if __name__ == "__main__":
    pass
