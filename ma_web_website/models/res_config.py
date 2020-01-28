 
 
from odoo import models, fields


class WebWebsiteConfigSettings(models.TransientModel):

    _inherit = 'res.config.settings'

    group_multi_website = fields.Boolean(
        string='Multi Website for Backend',
        help='Show Website Switcher in backend',
        implied_group='ma_web_website.group_multi_website')
