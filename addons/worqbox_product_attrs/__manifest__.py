# -*- coding: utf-8 -*-
{
    'name': "Worqbox Product Attrs",

    'summary': """
        Add new fields as attributs to product + Distigsh between LPL and Orac aatributes
    """,

    'description': """Add new fields as attributs to product + Distigsh between LPL and Orac aatributes """,

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
