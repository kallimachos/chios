#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables RST includes from remote sources.

Copyright 2017 Brian Moss
"""

import requests
from sphinx.directives import other

from chios import __version__


class RemoteInclude(other.Include):
    """Create remote-include directive."""

    def run(self):
        """Fetch remote RST."""
        link = self.content[0]
        try:
            r = requests.get(link)
            assert r.status_code == 200
            self.content = [r.text]
            return super(RemoteInclude, self).run()
        except:
            document = self.state.document
            err = 'Unable to resolve ' + link
            return [document.reporter.warning(str(err), line=self.lineno)]


def setup(app):
    """
    Setup for Sphinx extension.

    :param app: Sphinx application context.
    """
    app.info('adding remote-include directive...', nonl=True)
    app.add_directive('remote-include', RemoteInclude)
    app.info(' done')
    return {'version': __version__}


if __name__ == '__main__':
    pass
