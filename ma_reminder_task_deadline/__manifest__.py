{
    "name": "Reminders and Agenda for Tasks",
    "summary": """Allows you to create reminders for tasks.""",
    "category": "Reminders and Agenda",
     
    "version": "11.0.1.0.0",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "LGPL-3",
    "price": 7.00,
    "currency": "EUR",

    "depends": [
        "ma_reminder_base",
        "project",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/reminder_task_deadline_views.xml",
    ],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
