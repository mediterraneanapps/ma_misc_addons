{
    'name': "Oil odometer field on Vehicle form",

    'summary': """add Last oil change field""",


    'author': "Mediterranean Apps",
    'license': 'LGPL-3',
    'category': 'Managing vehicles',
    'version': '0.1',

    'depends': ['base', 'fleet'],

    'data': [
        'views/fleet_odometer_oil.xml',
    ],
    'demo': [
    ],
    'installable': True,
}
