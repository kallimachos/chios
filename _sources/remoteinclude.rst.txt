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
