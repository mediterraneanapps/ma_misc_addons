{
    'name': 'Email confirmation on sign up',
    'summary': """New user is able to login only after confirming his/her email""",
    'version': '1.0.1',
    'author': 'Mediterranean Apps',
    'license': 'LGPL-3',
    "price": 26.00,
    "currency": "EUR",
    'depends': [
        'auth_signup',
    ],
    'data': ['data/config.xml', 'views/thankyou.xml', 'data/email.xml'],
    'installable': False,
    'post_init_hook': 'init_auth',
}
