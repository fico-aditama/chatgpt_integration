# -*- coding: utf-8 -*-
{
    'name': "custom_module_sanqua",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Fiko Aditama",
    'website': "http://www.yourcompany.com",

    'category': 'Apps',
    'version': '14.0',

    'depends': ['base', 'purchase','sale_management','account','stock', 'contacts'],

    'data': [
        'security/ir.model.access.csv',
        'views/sale_report.xml',
        'views/model_sequence.xml',
        'views/views_contact.xml',
        'views/purchase_request.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
