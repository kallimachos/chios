========================
Chios test documentation
========================

bolditalic
~~~~~~~~~~

Lorem ipsum dolor sit amet, ea dico scribentur eos. No his detracto platonem
referrentur, debet timeam vix ut.

In this sentence :bolditalic:`there should be some bolditalic` text that
demonstrates the ``bolditalic`` role.

Nisl modo minim te nec. Congue theophrastus nam eu, cu fierent laboramus
evertitur ius.


remotecode
~~~~~~~~~~

Lorem ipsum dolor sit amet, ea dico scribentur eos. No his detracto platonem
referrentur, debet timeam vix ut.

**Directive used:**

.. code::

   .. remote-code-block:: ini

      https://raw.githubusercontent.com/kallimachos/chios/master/tests/example.ini

**Result:**

.. remote-code-block:: ini

   https://raw.githubusercontent.com/kallimachos/chios/master/tests/example.ini

**Directive used:**

.. code::

   .. remote-code-block:: ini

      https://example.ini

**Result:**

.. remote-code-block:: ini

   https://example.ini


remoteinclude
~~~~~~~~~~~~~

Lorem ipsum dolor sit amet, ea dico scribentur eos. No his detracto platonem
referrentur, debet timeam vix ut.

**Directive used:**

.. code::

   .. remote-include:: https://raw.githubusercontent.com/kallimachos/chios/master/tests/example.rst

**Result:**

.. remote-include:: https://raw.githubusercontent.com/kallimachos/chios/master/tests/example.rst


**Directive used:**

.. code::

   .. remote-include:: https://example.rst

**Result:**

.. .. remote-include:: https://example.rst
