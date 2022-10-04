.. _sphinx-extractor:

Sphinx-Extractor
================

A `Sphinx <https://www.sphinx-doc.org>`_ extension to extract 
`rst code <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_ from text-based files.
It is tested for file type of txt, py, puml, and md.

It uses directive :ref:`extract` to extract rst code from specified location in given file.

.. _usage:

Usage
-----

After :ref:`install` and :ref:`activate`, use directive :ref:`extract` in your rst files like below:


Extract from txt file
~~~~~~~~~~~~~~~~~~~~~

To extract rst code from the following example content of my.txt file:

.. code-block::

   This is example test txt file.

   @startrst
   .. code-block:: ruby

      Some Ruby code.

   .. note::

      something stuff to note.
   @endrst

Use the directive :ref:`extract` like following:

.. code-block:: rst

   .. extract:: ../tests/doc_test/utils/mytxt.txt
      :start: @startrst
      :end: @endrst

The directive :ref:`extract` block will be replaced with the extracted rst content:

.. extract:: ../tests/doc_test/utils/mytxt.txt
   :start: @startrst
   :end: @endrst

Extract from py file
~~~~~~~~~~~~~~~~~~~~

**Example python file content**

.. code-block::

   def my_app():
    """
    @rst
    .. code-block:: python

       Some python code.

       def dummy():
           pass
    @endrst
    """
    pass

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

   installation
   directives
   license
   changelog
