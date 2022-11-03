# -*- coding: utf-8 -*-
{
    'name': "ks_partner_report",

    'summary': """
        Invoiced partner rapport
    """,

    'description': """
        Invoiced partner rapport
    """,

    'author': "Marinah, KASIA SARLU",
    'website': "https://kasia.mg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'contacts',
                'account'

    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'report/partner_report.xml',
    ],

}
