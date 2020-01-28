{
    "name": """Preview Media Files""",
    "summary": """Open attached images in popup""",
    "category": "Web",
    "images": ['images/screenshot-1.png'],
    "version": "11.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 6.00,
    "currency": "EUR",

    "depends": [
        "ma_ir_attachment_url",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/web_preview_template.xml",
    ],
    "qweb": [
        "static/src/xml/media_tree_view_widget.xml",
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
