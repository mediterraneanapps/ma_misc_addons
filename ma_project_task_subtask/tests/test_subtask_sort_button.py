import odoo.tests
from odoo.api import Environment


@odoo.tests.common.at_install(True)
@odoo.tests.common.post_install(True)
class TestUi(odoo.tests.HttpCase):

    def test_01_subtask_sort_button(self):
        env = Environment(self.registry.test_cr, self.uid, {})
         
         
         
         
        env['ir.module.module'].search([('name', '=', 'project_task_subtask')], limit=1).state = 'installed'
         
        task = env['project.task'].search([('active', '=', 'true')], limit=1)
        url = '/web? 
        self.registry.cursor().release()

        code = """
            $(document).ready( function() {
                setInterval(function(){
                    if ($('.o_x2m_control_panel .o_cp_buttons .btn.o_pager_sort').length > 0) {
                        console.log('ok');
                    }
                }, 1000);
                setTimeout(function(){
                    if ($('.o_x2m_control_panel .o_cp_buttons .btn.o_pager_sort').length > 0) {
                        console.log('ok');
                    } else {
                        console.log(document.documentElement.innerHTML);
                        console.log('error', 'Sort Button is not displayed');
                    }
                }, 20000);
            });
        """
        self.phantom_js(url, code, login="admin")
