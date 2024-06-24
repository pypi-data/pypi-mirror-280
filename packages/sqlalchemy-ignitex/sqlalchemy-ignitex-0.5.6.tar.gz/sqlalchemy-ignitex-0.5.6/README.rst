
sqlalchemy-ignite
=================

This project provides an Apache Ignite dialect for SQLAlchemy.

Installation
------------

The package is installable through PIP::

   pip install sqlalchemy-igniteX

Usage
-----

>>> from sqlalchemy.engine import create_engine
>>> engine = create_engine("igniteworks://127.0.0.1:10800")


For more advanced access to Apache Ignite, including SSL, please refer
to the (documented) parameters of the Connection object.

Testing
-------

The dialect can be registered on runtime if you don't want to install it as::

>>>  from sqlalchemy.dialects import registry
>>>  registry.register("igniteworks", "igniteworks.sqlalchemy.dialect", "dialect")

