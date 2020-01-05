===============================================
 Context-dependent values in System Parameters
===============================================

Adds multi-company and multi-website support to many features

Based on built-in ``company_dependent`` and new ``website_dependent`` attributes. Real values are stored at ``ir.property``.

Check Usage instructions for understanding how it works.

Running auto-tests
==================

On following conditions:

* ``at_install`` tests are run in other modules
* during tests ``ir.config_parameter`` is used
* ``ir_config_parameter_multi_company`` is installed, but not loaded yet

The following error may appear::

    ERROR: column ir_config_parameter.value does not exist


To avoid it, add the module to ``--load`` parameter, e.g.::

    ./odoo-bin --load=web,ir_config_parameter_multi_company --test-enable -i some_module ...

Credits
=======

Contributors
------------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__

Sponsors
--------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps<mediterranean.apps@gmail.com>`__
