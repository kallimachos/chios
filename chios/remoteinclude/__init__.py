#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables RST includes from remote sources.

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

import requests
from sphinx.directives import other
from sphinx.util import logging

from chios import __version__

logger = logging.getLogger(__name__)


class RemoteInclude(other.Include):
    """Create remote-include directive."""

    def run(self):
        """Return rel path to a downloaded file as `include` node argument."""
        document = self.state.document
        env = document.settings.env
        buildpath = env.app.outdir
        link = self.arguments[0]

        try:
            r = requests.get(link)
            r.raise_for_status()
            downloadpath = os.path.join(buildpath, "_downloads")
            if not os.path.isdir(downloadpath):
                os.makedirs(downloadpath)
            rstfile = os.path.join(downloadpath, os.path.basename(link))
            with open(rstfile, "w") as f:
                f.write(r.text)
            rstfile = os.path.relpath(rstfile, os.path.dirname(env.doc2path(env.docname)))
            self.arguments = [rstfile]
            return super(RemoteInclude, self).run()
        except Exception:
            err = "Unable to resolve " + link
            return [document.reporter.warning(str(err), line=self.lineno)]


def setup(app) -> dict:
    """
    Set up Sphinx extension.

    :param app: Sphinx application context.
    """
    logger.info("adding remote-include directive...", nonl=True)
    app.add_directive("remote-include", RemoteInclude)
    logger.info(" done")
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


if __name__ == "__main__":
    pass
