{
    "name": """Compute Salary Inputs""",
    "summary": """Allows to compute amounts of inputs in salary rules""",
    "category": "Human Resources",
     
    "images": ["static/description/icon.png"],
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
     
     

    "depends": [
        'hr_payroll',
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'security/hr_rule_input_compute_security.xml',
        'views/hr_payroll_views.xml',
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
