{
    "name": """Reminders and Agenda for Opportunities (with time)""",
    "summary": """Reminders for opportunities with the precise time feature""",
    "category": "Reminders and Agenda",
    "images": [],
    "version": "10.0.1.0.1",
    "application": False,

    "author": "Mediterranean Apps",
    "support": "mediterranean.apps@gmail.com",
    "license": "GPL-3",
    "price": 7.00,
    "currency": "EUR",

    "depends": [
        "ma_reminder_base",
        "crm",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/views.xml",
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
