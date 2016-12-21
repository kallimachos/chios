#!/bin/python3
# coding: utf-8
"""Bolditalic test file."""

from sphinx_testing import TestApp as MakeApp  # rename to prevent warning

htmlfile = 'index.html'
result = ('<span class="bolditalic">there should be some bolditalic</span>')
cssresult = ('<link rel="stylesheet" ' +
             'href="_static/bolditalic.css" type="text/css" />')


def test_bolditalic():
    """Test bolditalic."""
    app = MakeApp(srcdir='tests/bitest', copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    html = (app.outdir / htmlfile).read_text()
    assert result in html


def test_css():
    """Test css."""
    app = MakeApp(srcdir='tests/bitest', copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    html = (app.outdir / htmlfile).read_text()
    assert cssresult in html


if __name__ == '__main__':
    pass
