#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables inline bold + italic.

https://github.com/kallimachos/chios

Copyright (C) 2021 Brian Moss

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
from shutil import copy

from docutils import nodes
from sphinx.util import logging

from chios import __version__

logger = logging.getLogger(__name__)


def css(app, env):
    """
    Add bolditalic CSS.

    :param app: Sphinx application context.
    :param env: Sphinx environment context.
    """
    srcdir = os.path.abspath(os.path.dirname(__file__))
    cssfile = "bolditalic.css"
    csspath = os.path.join(srcdir, cssfile)
    buildpath = os.path.join(app.outdir, "_static")
    try:
        os.makedirs(buildpath)
    except OSError:
        if not os.path.isdir(buildpath):
            raise
    copy(csspath, buildpath)
    app.add_css_file(cssfile)
    return


def bolditalic(name, rawtext, text, lineno, inliner, options=None, content=None):
    """
    Add bolditalic role.

    Returns 2 part tuple containing list of nodes to insert into the
    document and a list of system messages.  Both are allowed to be
    empty.

    :param name: The role name used in the document.
    :param rawtext: The entire markup snippet, with role.
    :param text: The text marked with the role.
    :param lineno: The line number where rawtext appears in the input.
    :param inliner: The inliner instance that called this function.
    :param options: Directive options for customization.
    :param content: The directive content for customization.
    """
    if options is None:
        options = {}
    if content is None:
        content = []
    node = nodes.inline(rawtext, text)
    node["classes"].append("bolditalic")
    return [node], []


def setup(app) -> dict:
    """
    Set up Sphinx extension.

    :param app: Sphinx application context.
    """
    try:
        logger.info("adding bolditalic role...", nonl=True)
        app.add_role("bolditalic", bolditalic)
        app.connect("env-updated", css)
        logger.info(" done")
    except Exception:
        logger.warning("Failed to initialize bolditalic styling.")
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


if __name__ == "__main__":
    pass
