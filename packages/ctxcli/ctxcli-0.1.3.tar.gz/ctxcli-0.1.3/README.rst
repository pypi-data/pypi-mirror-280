================================
CLI Tools for ConnectX
================================

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/connectX.png
   :alt: ConnectX Logo

.. contents:: Table of Contents
   :local:

Introduction
============

The ctxcli package provides Command Line Interface (CLI) tools for Amdocs ConnectX. These tools allow authorized ConnectX users to perform various operations on the system.

Installation
============

Before installing ctxcli, ensure that `Python <https://www.python.org/downloads/>`__ and `pip <https://pip.pypa.io/en/stable/installing/>`__ are installed on your system.

To install ctxcli from PyPI, use the following command::

    pip install ctxcli

Authentication
==============

Before running any command, you need to authenticate by running the 'auth' command. Use the following command to authenticate::

    ctxcli auth

You will be prompted to enter your tenant, environment (dev, ppe, prod), username, and password.

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/auth-screenshot.png
   :alt: Auth Screenshot

Commands
========

The ctxcli commands are divided into the following categories: Users, Tenant, and Migration.

Users
-----

To list all the users in the system, use the following command::

    ctxcli user list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/users-list-screenshot.png
   :alt: Users Screenshot

Tenant
------

To list all the sub-tenants in the system, use the following command::

    ctxcli tenant list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/tenants-list-screenshot.png
   :alt: Tenants Screenshot

Migration
---------

To list all the migration files in the system, use the following command::

    ctxcli migration file list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/migration-files-screenshot.png
   :alt: Migration Files Screenshot



Business Units
--------------

To list all the sub-tenants in the system, use the following command::

    ctxcli business-unit list

Here's an example of the output:

.. image:: https://assets.ppe.amdocs-dbs.cloud/ctxcli/business-units-screenshot.png
   :alt: Migration Files Screenshot


To add users to business units, use the following command::

	ctxcli business-unit add-users --file input\filename.csv
	
This command requires a CSV file that contains the necessary user information. The file can be placed in the “input” folder.
You can specify the path to this CSV file using the --file argument followed by the path to your file.
The CSV file should include two columns with headers:

    business_unit_id: The internal ID of the Business Unit to which you want to add users.
    username: The username of the user you want to add to the Business Unit.
    
The command will read each line of the CSV file and attempt to add the specified user to the corresponding Business Unit.


License
=======

Copyright 2024 Amdocs