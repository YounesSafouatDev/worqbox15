# -*- coding: utf-8 -*-
{
    'name': "NeoWall Product Attrs",

    'summary': """
        Add new fields as attributs to product for new company NeoWall
    """,

    'description': """Add new fields as attributs to product for new company NeoWall""",

    'author': "Worqbox",
    'website': "www.orac.com",

    'category': 'Sale',
    'version': '15.0.0.0.1',

    'depends': [
        'base',
        'sale',
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_attributes_views.xml',
        'views/menus.xml',
    ],
}
