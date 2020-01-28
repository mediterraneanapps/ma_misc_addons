{
    "name": "Import Settings",
    "version": "11.0.1.0.0",
    "summary": "Allows to save import settings to don't specify columns to fields mapping each time.",
    "category": "Extra Tools",
    "images": ["images/icon.png"],

    "author": "Mediterranean Apps",
    "license": "LGPL-3",
    "price": 30.00,
    "currency": "EUR",

    "depends": ["base_import"],
    "data": [
        "security/ir.model.access.csv",
        "views/base_import_map_templates.xml",
        "views/base_import_map_view.xml",
    ],
    "demo": [
    ],
    "installable": True,
    "auto_install": False,
}
