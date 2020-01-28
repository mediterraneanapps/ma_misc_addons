 
 

from odoo import models, api, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    odoobot_state = fields.Selection(string="Bot Status")

    @api.multi
    def is_admin(self):
         
         
        return self._is_admin()
