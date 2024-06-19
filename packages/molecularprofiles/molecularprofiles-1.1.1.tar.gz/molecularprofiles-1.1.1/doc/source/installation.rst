Installation
============

User Installation
-----------------

As a user, install from pypi:

.. code-block:: shell

    $ pip install molecularprofiles


Developer Setup
---------------

As a developer, clone the repository, create a clean conda environment 
and then install the package in development mode:

.. code-block:: shell

   $ git clone git@gitlab.cta-observatory.org:cta-array-elements/ccf/mdps.git
   $ cd mdps
   $ mamba create -n mdps -c conda-forge python==3.12 # you can also use conda instead of mamba
   $ mamba activate mdps
   $ pip install -e .[test,doc,dev]

The same also works with python's virtual environment (venv), you can use it instead of a conda environment.