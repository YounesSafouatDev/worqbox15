# -*- coding: utf-8 -*-
{
    'name': "worqbox_product_tech",

    'summary': """
        Product technical files for Worqbox
    """,

    'description': """
        Adds non mandatory product fields.
        They are displayed in a special tab which is shown depending of the company.

        WARNING : Requires to set an EXTERNAL_ID to the company to work:
            - ORAC : company_orac
    """,

    'author': "GIE",
    'website': "https://gie.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'stock',
        'worqbox_base',
        'worqbox_sale_default_uom'
    ],

    # always loaded
    'data': [
        'views/product_template_view.xml',
    ],
}
