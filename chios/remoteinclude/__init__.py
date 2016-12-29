#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables RST includes from remote sources.

Copyright 2017 Brian Moss
"""

import os

import requests
from sphinx.directives import other

from chios import __version__


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
            downloadpath = os.path.join(buildpath, '_downloads')
            if not os.path.isdir(downloadpath):
                os.makedirs(downloadpath)
            rstfile = os.path.join(downloadpath, os.path.basename(link))
            with open(rstfile, 'w') as f:
                f.write(r.text)
            rstfile = os.path.relpath(rstfile, os.path.dirname(env.doc2path
                                                               (env.docname)))
            self.arguments = [rstfile]
            return super(RemoteInclude, self).run()
        except:
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
