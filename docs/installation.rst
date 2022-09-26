.. _install:

Installation
============

Using pip
---------

.. code-block:: bash

   pip install sphinx-extractor

Using source code
-----------------

.. code-block:: bash

   git clone git@github.com:useblocks/sphinx-extractor.git
   cd sphinx-extractor
   pip install .

.. _activate:

Activation
----------

To use this extension, simply add `sphinx_extractor` to the project's extension list of your **conf.py** file.

.. code-block:: python

   extensions = ["sphinx_extractor",]
