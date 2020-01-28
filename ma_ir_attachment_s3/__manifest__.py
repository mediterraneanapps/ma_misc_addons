{
    "name": """S3 Attachment Storage""",
    "summary": """Upload attachments on Amazon S3""",
    "category": "Tools",
    "images": [],
    "version": "12.0.1.2.2",
    "application": False,

    "author": "Mediterranean Apps",
    "license": "AGPL-3",
    "price": 66.00,
    "currency": "EUR",

    "depends": [
        'base_setup',
        'ma_ir_attachment_url',
    ],
    "external_dependencies": {"python": ['boto3'], "bin": []},
    "data": [
        "data/ir_attachment_s3_data.xml",
        "security/ir.model.access.csv",
        "views/res_config_settings_views.xml",
    ],
    "qweb": [
    ],
    "demo": [
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
