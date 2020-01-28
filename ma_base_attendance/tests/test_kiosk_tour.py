import odoo.tests


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestKiosk(odoo.tests.HttpCase):

    def test_kiosk(self):
         
         
         
         
        env = self.env
        env['ir.module.module'].search([('name', '=', 'ma_base_attendance')], limit=1).state = 'installed'
         
         
        self.phantom_js("/web",
                        "odoo.__DEBUG__.services['web_tour.tour'].run('test_kiosk_tour', 500)",
                        "odoo.__DEBUG__.services['web_tour.tour'].tours.test_kiosk_tour.ready",
                        login="admin")
