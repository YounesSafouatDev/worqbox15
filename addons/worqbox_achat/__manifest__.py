# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'purchase order auto fill',
    'category':'purchase',
    'author': "Fillali Hafid",
    'summary': 'Manage purchase order automatique',
    'description': "gestion des achats automatique",
    'version': '1.0',
    'depends': ["purchase"],
    'data': [
        "views/purchase_order.xml",
        "security/ir.model.access.csv"
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
