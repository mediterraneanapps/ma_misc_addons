 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

{
    'name': 'Odoo Web Sessions Management Rules',
    'version': '1.0',
    'category': 'Tools',
    'sequence': 15,
    'summary': 'Manage Users Login Rules in Odoo.',
    'author': 'Mediterranean Apps',
    'depends': [
                'share',
                'base',
                'resource',
                'web',
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/scheduler.xml',
        'views/res_users_view.xml',
        'views/res_groups_view.xml',
        'views/ir_sessions_view.xml',
        'views/webclient_templates.xml',
    ],
    'init': [],
    'demo': [],
    'update': [],
    'test': [],   
    'installable': True,
    'application': False,
    'auto_install': False,   
    'certificate': '',
    "post_load": 'post_load',
}
