{
    'name': "Backend debranding",
    'version': '12.0.1.0.28',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'Debranding',
    'images': ['images/web_debranding.png'],
    'price': 83.00,
    'currency': 'EUR',
    'depends': [
        'web',
        'mail',
        'ma_access_settings_menu',
    ],
    'data': [
        'data.xml',
        'views.xml',
        'js.xml',
        'pre_install.xml',
    ],
    'qweb': [
        'static/src/xml/web.xml',
    ],
    "post_load": 'post_load',
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
    'installable': True,
    'saas_demo_title': 'Backend debranding demo',
}
