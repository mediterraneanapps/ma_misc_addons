{
    "name": """Project Task Checklist""",
    "summary": """Use checklist to be ensure that all your tasks are performed and to make easy control over them""",
    "category": """Project Management""",
    "images": ['images/checklist_main.png'],
    "version": "11.0.1.1.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "GPL-3",
    "price": 25.00,
    "currency": "EUR",

    "depends": ['base', 'project'],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'security/ir.model.access.csv',
        'views/project_task_subtask.xml',
        'views/assets.xml',
        'data/subscription_template.xml',
        'security/project_security.xml'
    ],
    "qweb": [
        'static/src/xml/templates.xml'
    ],
    "demo": [
        'demo/project_task_subtask_demo.xml'
    ],

    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,

    "auto_install": False,
    "installable": True,
}
