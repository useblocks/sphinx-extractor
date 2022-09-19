.. _sphinx-extractor:

Sphinx-Extractor
================

A `Sphinx <https://www.sphinx-doc.org>`_ extension to extract 
`rst code <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_ from text-based files.
It is tested for file type of txt, py, puml, and md.

It uses directive :ref:`extract` to extract rst code from specified location in given file.

.. _install:

Installation
------------

Using pip
~~~~~~~~~

.. code-block:: bash

   pip install sphinx-extractor

Using source code
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   git clone git@github.com:useblocks/sphinx-extractor.git
   cd sphinx-extractor
   pip install .

.. _usage:

Usage
-----

To use this extension, simply add `sphinx_extractor` to the project's extension list of your **conf.py** file.

.. code-block:: python

   extensions = ["sphinx_extractor",]

In your rst file, use directive :ref:`extract`.

.. _example:

Example
-------

Extract from txt file
~~~~~~~~~~~~~~~~~~~~~

**Example**

.. code-block:: rst

   .. extract:: ../tests/doc_test/utils/mytxt.txt
      :start: @startrst
      :end: @endrst

**Result**

.. extract:: ../tests/doc_test/utils/mytxt.txt
   :start: @startrst
   :end: @endrst

Extract from py file
~~~~~~~~~~~~~~~~~~~~

**Example**

.. code-block:: rst

   .. extract:: ../tests/doc_test/utils/myapp.py
      :start: @rst
      :end: @endrst

**Result**

.. extract:: ../tests/doc_test/utils/myapp.py
   :start: @rst
   :end: @endrst


.. toctree::
   :maxdepth: 2

   directives
   changelog
