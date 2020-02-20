# -*- coding: utf-8 -*-
{
    'name': "hey!",

    'summary': """
        Primer Módulo""",

    'description': """
        Prueba de creacion de mi primer módulo en Todoo!
    """,

    'author': "Robin Vega",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Módulo',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        #'views/templates.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #   'demo/demo.xml',
    #],
}
