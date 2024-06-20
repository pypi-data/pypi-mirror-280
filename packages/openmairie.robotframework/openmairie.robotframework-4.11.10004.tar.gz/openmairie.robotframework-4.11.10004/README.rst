openmairie.robotframework
=========================

RobotFramework Library for functional testing openMairie Framework based apps

.. image:: https://img.shields.io/pypi/v/openmairie.robotframework.svg
    :target: https://pypi.python.org/pypi/openmairie.robotframework/
    :alt: Latest PyPI version

.. contents::

Introduction
------------

openmairie.robotframework is a  `RobotFramework <http://robotframework.org/>`_
library who provide keywords to `openMairie Framework <http://www.openmairie.org/framework/>`_
based projects.


Installation
------------

You just need `pip <https://pip.pypa.io>`_ ::

    pip install openmairie.robotframework


Due to the history of this package all the keywords are declared in .robot
files. So you need to call the Reload Library in each Suite Setup. ::

    *** Settings ***
    Library  openmairie.robotframework.Library

    *** Keywords ***
    For Suite Setup
        Reload Library  openmairie.robotframework.Library


Keywords Documentation
----------------------

- https://openmairie.gitlab.io/openmairie.robotframework/


How to cross-validate ?
-----------------------

In order to fulfill the process of cross-validation before accepting the merge request:

1. Activate the virtual environment in which you wish to install the repository.

2. Install the repository to be tested on your system:

.. code-block:: bash

    pip install git+https://gitlab.com/openmairie/openmairie.robotframework.git@branch_name

3. Verify if the keywords affected by the changes are still functioning correctly.

In case of any doubts, revert to your original configuration using:

.. code-block:: bash

    pip uninstall openmairie.robotframework

To restore your original setup, use:

.. code-block:: bash

    pip install git+https://gitlab.com/openmairie/openmairie.robotframework.git