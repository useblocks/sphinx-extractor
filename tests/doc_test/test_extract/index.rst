Directive Extract test documentation
====================================


Test rst code extraction for all supported text-based file.

* puml file
* txt file
* md file
* python file

Puml file extract example
-------------------------

.. extract:: ../utils/myuml.puml
   :start: @rst
   :end: @endrst

Txt file extract example
------------------------

.. extract:: ../utils/mytxt.txt
   :start: @startrst
   :end: @endrst

Python file extract example
---------------------------

.. extract:: ../utils/myapp.py
   :start: @rst
   :end: @endrst

Markdown file extract example
-----------------------------

.. extract:: ../utils/mymd.md
   :start: ```{eval-rst}
   :end: ```

Example extract with absolute file path
---------------------------------------

.. extract:: /../utils/myuml.puml
   :start: @rst
   :end: @endrst
