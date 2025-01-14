# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Vendeur',
    'category':'vendeur',
    'author': "Fillali Hafid",
    'summary': 'Manage accounting of vendeur',
    'description': "gestion des vendeur Achat/vente",
    'version': '1.0',
    'depends': ["sale"],
    'data': [
        "views/achat.xml",
        "views/vente.xml",
        "views/vendeur.xml",
        "views/sale_order.xml",
        "views/res_user.xml",
        "security/ir.model.access.csv"
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
