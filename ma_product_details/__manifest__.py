{
    "name": """Product Details""",
    "summary": """Allows to add links with describes of products.""",
    "category": "Extra Tools",
    "images": ["static/description/icon.png"],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "license": "LGPL-3",
     
     

    "depends": [
        'product', 'ma_base_details',
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'views/product_detail.xml',
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
