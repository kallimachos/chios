#!/bin/python3
# coding: utf-8
"""Remoteinclude test file."""

from sphinx_testing import TestApp as MakeApp  # rename to prevent warning

htmlfile = 'index.html'
highlight = 'code'
sourcecode = 'This is some source RST'


def test_remoteinclude():
    """Test remoteinclude."""
    app = MakeApp(srcdir='tests/sample', copy_srcdir_to_tmpdir=True)
    app.builder.build_all()
    html = (app.outdir / htmlfile).read_text()
    assert highlight in html
    assert sourcecode in html


if __name__ == '__main__':
    pass
