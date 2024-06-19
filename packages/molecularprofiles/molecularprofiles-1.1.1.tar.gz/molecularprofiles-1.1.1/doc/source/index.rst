Welcome to ``molecularprofiles`` documentation!
===============================================

**Version**: |version| **Date**: |today|

This is molecularprofiles, a Python package that will help with the analysis of molecular profile data
obtained from global data assimilation systems, like GFS, GDAS, ECMWF or pre-processed data from WRF.

This library works with ``grib(1,2)`` or ``ecsv`` file formats, and is specifically designed
for the analysis of molecular content above the CTAO sites,
at El Roque de los Muchachos in the island of La Palma, and at Paranal in Chile.

The library helps the user to perform several tasks:

* Extract meteorological data and transform it from ``grib`` to ``ecsv`` format
* Analyze these data and produce atmospheric models
* Generate extinction input cards for the ``sim_telarray`` simulation package
* Some other utilities for time-series analysis

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   reference

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
