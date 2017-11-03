#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables code blocks from remote sources.

https://github.com/kallimachos/chios

Copyright (C) 2017 Brian Moss

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

import requests
from sphinx.directives import code

from chios import __version__


class RemoteCodeBlock(code.CodeBlock):
    """Create remote-code-block directive."""

    def run(self):
        """Fetch remote code."""
        link = self.content[0]
        try:
            r = requests.get(link)
            r.raise_for_status()
            self.content = [r.text]
            return super(RemoteCodeBlock, self).run()
        except Exception:
            document = self.state.document
            err = 'Unable to resolve ' + link
            return [document.reporter.warning(str(err), line=self.lineno)]


def setup(app):
    """
    Setup for Sphinx extension.

    :param app: Sphinx application context.
    """
    app.info('adding remote-code-block directive...', nonl=True)
    app.add_directive('remote-code-block', RemoteCodeBlock)
    app.info(' done')
    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        }


if __name__ == '__main__':
    pass
