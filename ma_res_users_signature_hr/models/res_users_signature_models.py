from odoo import api
from odoo import models


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    @api.multi
    def write(self, vals):
        res = super(HrEmployee, self).write(vals)
        for r in self:
            r.user_id.render_signature_id()
        return res
