{
    "name": """Partner Attendances""",
    "summary": """Manage partner attendances""",
    "category": "Extra Tools",
     
    "images": [],
    "version": "12.0.1.1.2",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 60.00,
    "currency": "EUR",

    "depends": [
        'barcodes'
    ],
    "external_dependencies": {"python": [], "bin": []},
    'data': [
        'security/res_attendance_security.xml',
        'security/ir.model.access.csv',
        'views/web_asset_backend_template.xml',
        'views/res_attendance_view.xml',
        'report/res_partner_badge.xml',
        'views/res_config_view.xml',
    ],
    'demo': [
    ],
    'qweb': [
        "static/src/xml/attendance.xml",
    ],
    'installable': True,
    'auto_install': False,
}
