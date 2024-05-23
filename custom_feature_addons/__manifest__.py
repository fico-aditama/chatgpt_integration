# -*- coding: utf-8 -*-
{
    'name': "Custom Addons",

    'summary': """
            * Photo Studio : background remover
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Fiko Aditama",
    'website': "https://www.yourcompany.com",
    'category': 'Studio',
    'version': '0.1',
    'depends': ['base', 'web_studio'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'external_dependencies': {
        'python': ['opencv-python', 'numpy', 'Pillow','rembg','PIL'],
    },
}
