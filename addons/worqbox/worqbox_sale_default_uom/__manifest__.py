# -*- coding: utf-8 -*-
{
    'name': "worqbox_sale_default_uom",

    'summary': """Choose a default UOM in product for sale orders""",

    'description': """
        Choose a UOM in product which will be used by default in sale orders.
    """,

    'author': "GIE",
    'website': "https://gie.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management'],

    # always loaded
    'data': [
        'views/product_template_views.xml',
    ],
    # only loaded in demonstration mode

}
