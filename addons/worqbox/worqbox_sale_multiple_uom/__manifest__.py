# -*- coding: utf-8 -*-
{
    'name': "worqbox_sale_multiple_uom",

    'summary': """Adjust the quantity in sale orders""",

    'description': """
        When selling with another UOM, update the quantity to match the multiple
        set in the product UOM by its rouding precision.
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
    ],
    # only loaded in demonstration mode

}
