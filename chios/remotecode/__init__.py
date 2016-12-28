#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables code blocks from remote sources.

Copyright 2017 Brian Moss
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
        except:
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
    return {'version': __version__}


if __name__ == '__main__':
    pass
