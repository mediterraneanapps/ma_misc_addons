{
    "name": "Attachment Url",
    "summary": """Use attachment URL and upload data to external storage""",
    "category": "Tools",
    "images": [],
    "version": "12.0.1.1.10",
    "application": False,

    "author": "Mediterranean Apps",
    "license": "AGPL-3",
    "price": 10.00,
    "currency": "EUR",

    "depends": [
        "web",
        "product",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "data/ir_attachment_url_data.xml",
        "views/ir_attachment_url_template.xml",
        "views/ir_attachment_res_config.xml",
        "demo/ir_attachment.xml",
    ],
    "qweb": [
        "static/src/xml/ir_attachment_url.xml",
    ],
    "demo": [
    ],

    "post_load": "post_load",
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
