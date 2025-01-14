# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'avoir commande ',
    'category':'sales',
    'author': "Fillali Hafid",
    'summary': '',
    'description': "",
    'version': '1.0',
    'depends': ["sale"],
    'data': [
        "views/sale_order.xml",
        "security/ir.model.access.csv"
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
