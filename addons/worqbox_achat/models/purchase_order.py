# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
from odoo import api, fields, models
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    def action_achat(self):
        purchaseid = self.id
        productVariants = self.env['product.template']
        products = productVariants.search([('reordering_min_qty', '>', 0),('company_ids', 'in', 11)])
        for rec in products:
            if rec.reordering_min_qty > 0 or rec.virtual_available < 0 :
                qtycom = 0
                qtycom = rec.reordering_min_qty - rec.virtual_available
                if qtycom > 0:
                    getprodid = self.env['product.product'].sudo().search([('product_tmpl_id', '=', rec.id)])
                    getpackid = self.env['product.packaging'].sudo().search([('product_id', '=', getprodid.id)])
                    checkprod = self.env['purchase.order.line'].sudo().search([('product_id', '=', getprodid.id), ('order_id', '=', purchaseid)])
                    
                    if checkprod:
                        checkprod.sudo().update({'product_qty': qtycom})
                    else:
                        if getpackid:
                            self.env['purchase.order.line'].sudo().create(
                                {
                                    'product_id': getprodid.id,
                                    'product_qty': qtycom,
                                    'product_packaging_qty':qtycom / getpackid[0].qty ,
                                    'product_packaging_id':getpackid[0].id,
                                    'order_id': purchaseid
                                })
                        else:
                             self.env['purchase.order.line'].sudo().create(
                                {
                                    'product_id': getprodid.id,
                                    'product_qty': qtycom,
                                    'order_id': purchaseid
                                })