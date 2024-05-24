# -*- coding: utf-8 -*-
{
    'name': "Custom Dashboard",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Fiko Aditama",
    'website': "https://www.yourcompany.com",
    'category': 'Apps',
    'version': '0.1',
    'depends': ['base','web','sale', 'board','spreadsheet_dashboard_sale',],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/sales_dashboard.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_dashboard/static/src/**/**/*.js',
            'custom_dashboard/static/src/**/**/*.xml',
            'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.9.4/Chart.js',
            'https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css',
        ],
    },
    'auto_install': ['spreadsheet_dashboard_sale'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
