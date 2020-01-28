 
 
from odoo import models, fields, api

FIELDS = ['foo', 'user_id']


class WebsiteDependent(models.Model):
    _inherit = 'website_dependent.mixin'
    _name = 'test.website_dependent'

    name = fields.Char()
    foo = fields.Char(company_dependent=True, website_dependent=True)
    user_id = fields.Many2one('res.users', company_dependent=True, website_dependent=True)

    @api.model
    def create(self, vals):
        res = super(WebsiteDependent, self).create(vals)
         
        for f in FIELDS:
            res._force_default(f, vals.get(f))
        return res

    @api.multi
    def write(self, vals):
        res = super(WebsiteDependent, self).write(vals)

        if 'name' in vals:
            fields_to_update = FIELDS
        else:
            fields_to_update = [
                f for f in FIELDS
                if f in vals
            ]
        for f in fields_to_update:
            self._update_properties_label(f)

        return res


class CompanyDependent(models.Model):
    _name = 'test.company_dependent'
    _description = 'Test Class with company_dependent fields'

    foo = fields.Char(company_dependent=True)
    user_id = fields.Many2one('res.users', company_dependent=True)
