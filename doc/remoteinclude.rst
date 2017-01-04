=============
remoteinclude
=============

**remoteinclude** is an extension for Sphinx that enables RST file inclusion
from remote sources.

.. warning::

   Including text from a remote source is a security risk, as the text is
   parsed after inclusion. Include files from trusted sources only.


Usage
~~~~~

#. :ref:`Install chios <install>`, then add **remoteinclude** to the list of
   extensions in ``conf.py``:

   .. code::

      extensions = ['chios.remoteinclude']

#. Use the ``remote-include`` directive to fetch a remote RST file and
   include it:

   .. code::

      .. remote-include:: https://example.com/rawsource.rst

   .. important::

      The ``remote-include`` directive does not follow references to other
      remote files within a downloaded file. In other words, ``toctree``,
      ``:ref:``, and similar markup fails because the referenced files are not
      locally available.


Using a remote file in a toctree
--------------------------------

The ``toctree`` directive does not allow ``include`` as a child. To use a
remote file in a ``toctree``:

#. Create an RST file in your source directory with an appropriate name:

   .. code::

      $ touch doc/myfile.rst

#. Use the ``remote-include`` directive in that file:

   .. code::

      .. remote-include:: www.example.com/myfile.rst

#. You can now reference the local file in a ``toctree``:

   .. code::

      .. toctree::

         intro.rst
         chapter.rst
         myfile.rst


Troubleshooting
~~~~~~~~~~~~~~~

If a ``remote-include`` is empty in the HTML output, it is likely that
the given link could not be resolved. Check the Sphinx build messages for a
warning:

.. code::

   index.rst:32: WARNING: Unable to resolve https://example.com/rawsource.rst


Code listing
~~~~~~~~~~~~

.. automodule:: remoteinclude
   :members:
