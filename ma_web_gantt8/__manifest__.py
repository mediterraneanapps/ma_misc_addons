{
    "name": """Gantt view from odoo 8""",
    "summary": """Ported view from odoo 8""",
    "category": "Hidden",
    "images": [],
    "version": "1.0.1",

    "author": "Mediterranean Apps",
    "license": "AGPL-3",
    "price": 8.00,
    "currency": "EUR",

    "depends": [
        "web",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/web_gantt.xml',
    ],
    "qweb": [
        'static/src/xml/*.xml',
    ],
    "demo": [],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "installable": True,
    "auto_install": False,
    "application": False,
}
