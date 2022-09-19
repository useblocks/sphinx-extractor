.. _directives:

Directives
==========

.. _extract:

extract
-------

This directive `extract` takes an absolute or relative file path as argument and has 2 options:

* `start`: required, specify the start location string pattern
* `end`: required, specify the end location string pattern

.. code-block:: rst

   .. extract:: <file path>
      :start: <start location string>
      :end: <end location string>


Example
~~~~~~~

To extract content from following example plantuml file, e.g. `myuml.puml`:

.. code-block:: 

   @startuml
   @rst
   .. note::

      This is a sphinx default directive of note.
   @endrst
   @enduml


**Example usage of extract**

.. code-block:: rst

   .. extract:: ../tests/doc_test/utils/myuml.puml
      :start: @rst
      :end: @endrst

**Result**

.. extract:: ../tests/doc_test/utils/myuml.puml
   :start: @rst
   :end: @endrst
