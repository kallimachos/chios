==========
remotecode
==========

**remotecode** is an extension for Sphinx that enables code blocks from
remote sources.


Usage
~~~~~

#. :ref:`install` **chios**, then add **remotecode** to the list of extensions
   in ``conf.py``:

   .. code::

      extensions = ['chios.remotecode']

#. Use the ``remote-code-block`` directive to fetch remote source code and
   display it in a ``code-block``.

   .. code::

      .. remote-code-block:: ini

         https://example.com/rawsource.ini


Troubleshooting
~~~~~~~~~~~~~~~

If a ``remote-code-block`` is empty in the HTML output, it is likely that
the given link could not be resolved. Check the Sphinx build messages for a
warning:

.. code::

   index.rst:32: WARNING: Unable to resolve https://example.ini


Code listing
~~~~~~~~~~~~

.. automodule:: __init__
   :members:
