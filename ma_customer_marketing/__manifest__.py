{
    "name": """Customer Marketing""",
    "summary": """Allows to store detailed information about customers""",
    "category": "Marketing",
     
    "images": ["static/description/icon.png"],
    "version": "1.0.0",
    "application": False,
    "author": "Mediterranean Apps",
   "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
     
     

    "depends": [
        "contacts",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/res_partner_views.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": False,
}
