==========
bolditalic
==========

**bolditalic** is an extension for Sphinx that enables inline bold + italic
text styling.


Usage
~~~~~

#. :ref:`Install chios <install>`, then add **bolditalic** to the list of
   extensions in ``conf.py``:

   .. code::

      extensions = ['chios.bolditalic']

#. Use the ``bolditalic`` role to style text:

   .. code::

      The end of this sentence :bolditalic:`displays in bold and italic`.

.. important::

   If you define ``html_context`` in your ``conf.py``, you must add the
   ``bolditalic.css`` style sheet to it.

   **Example**

   .. code::

      html_context = {
        'css_files': [
          '_static/bespoke.css',  # custom CSS styling
          '_static/bolditalic.css',  # bolditalic styling
          ],
        }


Code listing
~~~~~~~~~~~~

.. automodule:: bolditalic
   :members:
