# -*- coding: utf-8 -*-
{
    'name': "Custom POS",

    'summary': """
        * Showing WB Button and WB Button2 POS
        * Pos Edit button in model post config "Visible Backspace Button"
        * Invisible (x) Numpad POS
        * Create Pop Up Odoo POS 
        * Translation id_ID.po
""",

    'description': """
        Long description of module's purpose
    """,
    'author': "Fiko Aditama",
    'website': "https://www.yourcompany.com",
    'category': 'Point of Sale',
    'version': '0.1',
    'depends': ['base','point_of_sale'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets' : {
        'point_of_sale.assets':[
            "custom_pos/static/src/js/wb_button.js",
            "custom_pos/static/src/js/wb_NumpadWidget.js",
            "custom_pos/static/src/xml/web_sample_button.xml",
            "custom_pos/static/src/xml/NumpadWidget.xml",
        ]
    }
}
