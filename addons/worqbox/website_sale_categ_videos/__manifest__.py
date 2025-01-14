# -*- coding: utf-8 -*-
{
    'name': "website_sale_categ_videos",

    'summary': """
        Add video urls to website category and show them in every products
    """,

    'description': """
        Add video urls to website category and show them in every products
    """,

    'author': "GIE",
    'website': "https://gie.ma",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '15.0.0.0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'website_sale',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/website_sale_product.xml',
        'views/product_public_category.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'website_sale_categ_videos/static/src/scss/style.scss',
        ],
    },
}
