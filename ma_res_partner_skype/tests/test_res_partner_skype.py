import odoo.tests


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_res_partner_skype(self):
         
         
        env = self.env
        env['ir.module.module'].search([('name', '=', 'ma_res_partner_skype')], limit=1).state = 'installed'
        env['res.partner'].search(([('id', '=', 9)]), limit=1).write({
            'skype': 'skype_test',
        })

         
         
        self.phantom_js("/web 
                        "odoo.__DEBUG__.services['web_tour.tour'].run('tour_res_partner_skype', 1000)",
                        "odoo.__DEBUG__.services['web_tour.tour'].tours.tour_res_partner_skype.ready",
                        login="admin", timeout=300)
