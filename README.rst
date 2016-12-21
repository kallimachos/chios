=====
chios
=====

.. image:: https://travis-ci.org/kallimachos/chios.svg?branch=master
   :target: https://travis-ci.org/kallimachos/chios

.. image:: https://img.shields.io/pypi/status/chios.svg?style=flat
   :target: https://pypi.python.org/pypi/chios

.. image:: https://img.shields.io/pypi/v/chios.svg?style=flat
   :target: https://pypi.python.org/pypi/chios

.. image:: https://img.shields.io/badge/Python-2.7-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: https://img.shields.io/badge/Python-3-brightgreen.svg?style=flat
   :target: http://python.org

.. image:: http://img.shields.io/badge/license-GPL-blue.svg?style=flat
   :target: http://opensource.org/licenses/GPL-3.0

**chios** is a collection of Sphinx extensions named after the Greek island
Chios, whose symbol was the Sphinx.

Full documentation: https://kallimachos.github.io/chios/


Installation
~~~~~~~~~~~~

Install **chios** using ``pip``:

.. code::

   $ pip install chios


bolditalic
~~~~~~~~~~

**bolditalic** is an extension for Sphinx that enables inline bold + italic
text styling.

Full documentation: https://kallimachos.github.io/bolditalic/

Usage
-----

#. Add the **bolditalic** extension to the list of extensions in ``conf.py``:

   .. code::

      extensions = ['chios.bolditalic']

#. Use the ``bolditalic`` role to style text:

   .. code::

      The end of this sentence :bolditalic:`displays in bold and italic`.


remotecode
~~~~~~~~~~

**remotecode** is an extension for Sphinx that enables code blocks from
remote sources.

Full documentation: https://kallimachos.github.io/remotecode/

Usage
-----

#. Add **remotecode** to the list of extensions in ``conf.py``:

   .. code::

      extensions = ['chios.remotecode']

#. Use the ``remote-code-block`` directive to fetch remote source code and
   display it in a ``code-block``.

   .. code::

      .. remote-code-block:: ini

         https://example.com/rawsource.ini
