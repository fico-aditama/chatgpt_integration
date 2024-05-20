# -*- coding: utf-8 -*-
{
    'name': "Custom POS",

    'summary': """
        * Showing WB Button and WB Button2 POS
        * Pos Edit button in model post config "Visible Backspace Button"
        * Visible (x) Numpad POS
""",

    'description': """
        Long description of module's purpose
    """,
    'author': "Fiko Aditama",
    'website': "https://www.yourcompany.com",
    'category': 'Apps',
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
    'assets' : {
        'point_of_sale.assets':[
            "custom_pos/static/src/js/wb_button.js",
            "custom_pos/static/src/js/wb_NumpadWidget.js",
            "custom_pos/static/src/xml/web_sample_button.xml",
            "custom_pos/static/src/xml/NumpadWidget.xml",
        ]
    }
}
