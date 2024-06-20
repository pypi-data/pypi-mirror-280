NEMO Library
============

This library helps you with access to NEMO APIs

Installation
============

::

   pip install nemo_library

Sources
=======

please find all sources on github:
https://github.com/H3rm1nat0r/nemo_library

configuration
=============

please create a file “config.ini”. This is an example for the content:

::

   [nemo_library]
   nemo_url = https://enter.nemo-ai.com
   tenant = <your tenant>
   userid = <your userid>
   password = <your password>
   environment = [prod|dev|demo]

Methods
=======

Projects
--------

getProjectList method
~~~~~~~~~~~~~~~~~~~~~

Return list of projects (as pandas Dataframe)

.. code:: python

   from nemo_library import NemoLibrary

   nl = NemoLibrary()
   df = nl.getProjectList()

ProjectProperty method
~~~~~~~~~~~~~~~~~~~~~~

Get a project property

.. code:: python

   from nemo_library import NemoLibrary

   nl = NemoLibrary()
   val = nl.ProjectProperty(projectname=None,propertyname="ExpDateTo")

getImportedColumns method
~~~~~~~~~~~~~~~~~~~~~~~~~

Get list if imported columns of a project

.. code:: python

   from nemo_library import NemoLibrary
   import pandas as pd

   nl = NemoLibrary()
   df = nl.getImportedColumns(projectname="0 SNR")

setMetadataSortOrder method
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set sort order of fields in a project

.. code:: python

   from nemo_library import NemoLibrary
   import pandas as pd

   # import field order from infozoom meta data export
   dfsort = pd.read_csv("Metadaten_AUTODATA_SORT_1.csv",delimiter=";")
   fieldlist = dfsort["Importname"].to_list()

   nl = NemoLibrary()
   nl.setMetadataSortOrder(projectname="AUTODATA",fields=fieldlist)

ReUploadFile method
~~~~~~~~~~~~~~~~~~~

ReUpload a CSV file into an existing project

.. code:: python

   from nemo_library import NemoLibrary

   nl = NemoLibrary()
   nl.ReUploadFile(projectname="21 CRM", filename="./csv/hubspot.csv")

Reports
-------

LoadReport method
~~~~~~~~~~~~~~~~~

Load a report from NEMO and return this as pandas dataframe

.. code:: python

   from nemo_library import NemoLibrary

   nl = NemoLibrary()
   df = nl.LoadReport(report_guid="b82cfed8-81a7-44e0-b3da-c76454540697")

project_id
^^^^^^^^^^

Optional parameter. If you want to get reports for non-default ERP
projects. Please provide the project GUID (you can retrieve them by
running getProjectList)

report_guid
^^^^^^^^^^^

This methode takes 1 mandatory parameter, the report_guid. You can find
“your” guid in NEMO meta data. Just open the definition of the report in
meta data and copy the GUID from your browser URL.

The report “(SAMPLE) Replenishment Time Analysis Purchased Parts” for
example has this URL:
https://enter.nemo-ai.com/nemo/metadata/report/b82cfed8-81a7-44e0-b3da-c76454540697
and thus the GUID you need is then
“b82cfed8-81a7-44e0-b3da-c76454540697”

max_pages
^^^^^^^^^

By default all pages from the report are loaded. You can optionally
restrict the amount of data by providing max_pages parameter and you’ll
get not more than this number of pages (usually 1 page holds 20 records)

Contributions
=============

Contributions are welcome! If you would like to suggest improvements or
have found a bug, please open an issue or submit a pull request.

License
=======

This project is released under the Unlicense. You can find the full text
of the Unlicense in the `UNLICENSE <UNLICENSE>`__ file. This means that
the code is released into the public domain, and you are free to use,
modify, distribute, and do whatever you want with it, without any
restrictions or requirements.
