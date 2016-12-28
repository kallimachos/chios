#!/bin/python3
# coding: utf-8
"""
A Sphinx extension that enables RST includes from remote sources.

Copyright 2017 Brian Moss
"""

import requests
from sphinx.directives import other

import os

from chios import __version__


class RemoteInclude(other.Include):
    """Create remote-include directive."""

    def run(self):
        document = self.state.document
        if not document.settings.file_insertion_enabled:
            return [document.reporter.warning('File insertion disabled', line=self.lineno)]

        # try:
        link = self.arguments[0]
        tempfile = downloadfile(link)

        self.arguments = [tempfile]
        return super(RemoteInclude, self).run()
        # except:
        #     err = 'Unable to resolve ' + link
        #     return [document.reporter.warning(str(err), line=self.lineno)]


def downloadfile(link):
    """Download a remote file and save to the build path."""
    r = requests.get(link)
    r.raise_for_status()
    staticpath = os.path.join(buildpath, '_downloads')
    tempfile = os.path.join(staticpath, 'tempfile.rst')
    try:
        os.makedirs(staticpath)
    except OSError:
        if not os.path.isdir(staticpath):
            return [document.reporter.warning('bugger')]
    with open(tempfile, 'w') as f:
        f.write(r.text)
    return tempfile


def setup(app):
    """
    Setup for Sphinx extension.

    :param app: Sphinx application context.
    """
    app.info('adding remote-include directive...', nonl=True)
    global buildpath
    buildpath = app.outdir
    app.info(buildpath)
    app.add_directive('remote-include', RemoteInclude)
    app.info(' done')
    return {'version': __version__}


if __name__ == '__main__':
    pass
