# -*- coding: utf-8 -*-
{
    'name': "DRAGON TEST",

    'summary': """
        la description de mon module
    """,

    'description': """
        This module processes students management
    """,

    'author': "Kasia",
    'website': "http://kasia.mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'security/student.class.csv',
        'views/student_base_views.xml',
        'views/student_class_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
