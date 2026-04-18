{
    'name': 'Quick Actions: Reset Invoice to Draft',
    'version': '17.0.1.0.0',
    'summary': 'Instantly reset any posted invoice or bill back to Draft state.',
    'description': """
Quick Actions: Reset Invoice to Draft
======================================
A free utility module by BrimstoneTech that adds a single
"Reset to Draft" button directly onto any posted invoice or
vendor bill in Odoo 17 Community. 

Key Features:
- One-click reset to Draft state for mistakes.
- Simple, zero-configuration install.
- No third-party dependencies.

Developed by BrimstoneTech | Support: brimstonetech1@gmail.com | +256 744 429 293
""",
    'author': 'BrimstoneTech',
    'website': 'https://www.brimstonetech.com',
    'support': 'brimstonetech1@gmail.com',
    'category': 'Accounting/Accounting',
    'depends': ['account'],
    'data': [
        'views/account_move_views.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'license': 'OPL-1',
}
