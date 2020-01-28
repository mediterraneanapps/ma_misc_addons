{
    'name': 'Initialization data',
    'version': '1.0.0',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'Other',
    'depends': ['l10n_sg',
                'pitch_booking',
                'multi_company',
                'sms_sg',
                'ma_sale_order_hide_tax',
                'ma_res_partner_phone',
                'account_analytic_analysis',
                'booking_calendar_analytic',
                'website_sale_order_company',
                'invoice_sale_order_line_group',
                ],
    'data': [
        'data.xml',
        'views/view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}
