 
from . import models


def post_init_hook(cr, registry):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})

     
    env.cr.execute("ALTER TABLE test_website_dependent ADD COLUMN foo VARCHAR")
    env.cr.execute("ALTER TABLE test_website_dependent ADD COLUMN user_id INTEGER")
