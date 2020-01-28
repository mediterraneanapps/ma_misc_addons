from . import models

def uninstall_hook(cr, registry):
    from odoo import api, SUPERUSER_ID

    env = api.Environment(cr, SUPERUSER_ID, {})

     
    field_id = env.ref('base.field_ir_config_parameter__value').id
    env['ir.property'].search([('fields_id', '=', field_id)]).unlink()

     
    env['ir.module.module'].search([('name', '=', 'base')]).button_upgrade()
