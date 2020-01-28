from odoo import fields, models


class lead(models.Model):
    _name = "crm.lead"
    _inherit = ["crm.lead", 'pad.common']
    description = fields.Text('Notes', track_visibility=False)
    description_pad = fields.Char('Description PAD', pad_content_field='description')
