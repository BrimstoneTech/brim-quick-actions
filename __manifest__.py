{
    'name': 'Quick Actions: Reset Invoice to Draft',
    'version': '17.0.1.0.0',
    'price': 0.00,
    'currency': 'USD',
    'license': 'LGPL-3',
    'summary': 'Reset a posted invoice to draft in one click. No more multi-step cancellation.',
    'description': """
Quick Actions: Reset Invoice to Draft
======================================
A free utility module by BrimstoneTech that adds a single
"Reset to Draft" button directly onto any posted invoice or
vendor bill in Odoo 17 Community. Saves time, reduces clicks,
and is restricted to Accounting Managers so your data stays safe.

What it does:
- Adds a bright "Reset to Draft" button on posted invoices/bills.
- The button is visible only to users with the Accounting Manager role.
- Internally calls the standard Odoo cancel and draft methods safely.
- No third-party dependencies. Community Edition safe.

By BrimstoneTech - brimstonetech1@gmail.com
    """,
    'author': 'BrimstoneTech',
    'website': 'https://apps.odoo.com',
    'support': 'brimstonetech1@gmail.com',
    'category': 'Accounting/Accounting',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/icon.png'],
}
