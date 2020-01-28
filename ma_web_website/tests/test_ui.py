 
 
from odoo.tests import common, tagged


@tagged('at_install', 'post_install')
class TestUI(common.HttpCase):

    def test_ui(self):
         

         
         
         
         
        phantom_env = self.env
        phantom_env['ir.module.module'].search(
            [('name', '=', 'web_website')], limit=1
        ).state = 'installed'

         
        phantom_env.user.company_id = self.env.ref('base.main_company')
        phantom_env.user.website_id = None

        tour = 'web_website.tour'
        self.phantom_js(
            '/web',
            "odoo.__DEBUG__.services['web_tour.tour']"
            ".run('%s')" % tour,

            "odoo.__DEBUG__.services['web_tour.tour']"
            ".tours['%s'].ready" % tour,

            login='admin',
        )
