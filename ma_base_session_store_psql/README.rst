==============================
 Store sessions in postgresql
==============================

Odoo uses ``werkzeug.contrib.sessions.FilesystemSessionStore`` that lead to periodic "Session Expired" errors on disributed deployment. Saving sessions in postgresql fixes this issue.

Roadmap
=======

* Some good ideas can be taken from `session_db <https://github.com/odoo/odoo-extra/blob/master/session_db/models/session.py>`_ module

Credits
=======

Contributors
------------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

Sponsors
--------
* `Mediterranean Apps <mediterranean.apps@gmail.com>`__

