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


Extensions
~~~~~~~~~~

bolditalic
----------

Enables inline bold + italic text styling using a ``bolditalic`` role:

.. code::

   The end of this sentence :bolditalic:`displays in bold and italic`.

remotecode
----------

Enables code blocks from remote sources using a ``remote-code-block``
directive:

.. code::

   .. remote-code-block:: ini

      https://example.com/rawsource.ini

remoteinclude
-------------

Enables RST file inclusion from remote sources using a ``remote-include``
directive:

.. code::

   .. remote-include:: https://example.com/rawsource.rst
