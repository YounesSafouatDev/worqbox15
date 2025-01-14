# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models,api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    avoir_count = fields.Integer(compute="_avoir_count", string='Avoir', store=True) 


    def _avoir_count(self):
     for Saleorder in self:   
        i = 0  
        for invoice in Saleorder.invoice_ids :
            if 'RFAC' in invoice.name: 
                i += 1
        Saleorder.avoir_count = i 

    def get_avoir(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Avoir',
            'view_mode': 'tree',
            'res_model': 'account.move',
            'domain': [('invoice_origin', 'like', self.name) , ('type_name', 'like', 'Credit Note')]
        }



