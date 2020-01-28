{
    'name': 'Signature templates for user emails',
    'external_dependencies': {
        'python': [
            'bs4',
            'html2text',
        ],
    },
    'version': '12.0.1.0.0',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    'category': 'Social Network',
    'images': ["images/main.png"],
    'depends': ['base'],
    'data': [
        'views/res_users_signature_views.xml',
        'security/res_users_signature_security.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [
    ],

    'installable': True
}
