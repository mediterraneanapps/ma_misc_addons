.. image:: https://img.shields.io/badge/license-LGPL--3-blue.png
   :target: https://www.gnu.org/licenses/lgpl
   :alt: License: LGPL-3

=============================
 Website Switcher in Backend
=============================

Technical module to switch Websites in Backend similarly to Company Switcher. On changing it update field **backend_website_id** in ``res.users``.

website_dependent
=================

The module adds new field attribute ``website_dependent``, which is analog of ``company_dependent``, but for websites.

See `<models/test_website.py>`_ and `<tests/test_website_dependent.py>`_ to understand how it works.

If you need to convert existing field to a website-dependent field it's not
enough just to add the attributes. You need additional stuff to make your module
safely installable and uninstallable. See module
``ma_ir_config_parameter_multi_company`` as an example. Things to do:

* extend ``ir.property``'s ``write`` to call ``_update_db_value_website_dependent``
* Add to the field both ``company_dependent=True`` and ``website_dependent=True``
* In the field's module extend following methods:

  * ``create`` -- call ``_force_default``
  * ``write`` -- call ``_update_properties_label``
  * ``_auto_init`` -- call ``_auto_init_website_dependent``

* In the field's module add ``uninstall_hook``:

  * remove field's properties

Roadmap
=======

* TODO: Use context on switching between websites to allow work with different
  websites at the same time by using different browser tabs. It also fixes
  problem of using superuser's configuration when ``sudo()`` is used.

* TODO: Since odoo 12, there is another switcher at ``[[ Website ]] >> Dashboard`` menu. It has to be syncronized with the switcher of this module, i.e. hide default one and use value of this module switcher.

Credits
=======

Contributors
------------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

Sponsors
--------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

Maintainers
-----------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__