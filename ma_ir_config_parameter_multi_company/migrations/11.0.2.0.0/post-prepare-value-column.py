from odoo import api, SUPERUSER_ID


def migrate(cr, version):
     
     
     
     
    env = api.Environment(cr, SUPERUSER_ID, {})

    field_id = env.ref('base.field_ir_config_parameter__value').id
    default_values = env['ir.property'].search([
        ('fields_id', '=', field_id),
        ('company_id', '=', False)
    ])

    field = env.ref('base.field_ir_config_parameter__value')
    default_values._update_db_value_website_dependent(field)
