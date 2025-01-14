# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from collections import defaultdict
import base64
from odoo import api, fields, models
from odoo.http import request


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    achat_vendeur = fields.Many2one('vendeur.achat', 'Devis Origine')

    
    def action_colle(self):
        comp700=0
        comp500=0
        comp400=0
        comp300=0
        for record in self:
            for line in record.order_line :
                if line.product_id.categ_id.id == 301 or line.product_id.categ_id.id == 302:
                  comp700 = comp700 + line.product_uom_qty
                  comp400 = comp400 + line.product_uom_qty
                  comp300 = comp300 + line.product_uom_qty
                if  line.product_id.categ_id.id == 303 :
                  if line.product_id.id == 2049 or line.product_id.id == 2050 or line.product_id.id == 2045 or line.product_id.id == 2046 or line.product_id.id == 5878:
                    comp700 = comp700 + (line.product_uom_qty * 2)
                  else:
                    comp700 = comp700 + line.product_uom_qty 
                if line.product_id.categ_id.id == 304 : 
                   comp700 = comp700 + line.product_uom_qty  
                if line.product_id.categ_id.id == 300 or line.product_id.categ_id.id == 299  :
                  comp500 = comp500 + line.product_uom_qty
                  comp400 = comp400 + line.product_uom_qty
                  comp300 = comp300 + line.product_uom_qty
            for line in record.order_line :
                if line.product_id.id == 5744 and comp700 > 0:
                    i = int(comp700 / 8)
                    i = float(i)
                    if (comp700 / 8) > i :
                      i +=  1
                    line.update({'product_uom_qty':  i  })
                if line.product_id.id == 2126 and comp500 > 0:
                    i = int(comp500 / 8)
                    i = float(i)
                    if (comp500 / 8) > i :
                      i +=  1
                    line.update({'product_uom_qty':  i  })
                if line.product_id.id == 13388 and comp300 > 0:
                    i = int(comp300 / 30)
                    i = float(i)
                    if (comp300 / 30) > i :
                      i +=  1
                    line.update({'product_uom_qty':  i  })
                if line.product_id.id == 17453 and comp400 > 0:
                    i = int(comp400 / 80)
                    i = float(i)
                    if (comp400 / 80) > i :
                      i +=  1
                    line.update({'product_uom_qty':  i  })
  
    
    def action_confirm(self):
         for recod in self:
              confirm =super(SaleOrder,self).action_confirm()
              achat = recod.achat_vendeur
              recod.achat_vendeur.state = 'Devis Confirmer'
              pdf, _ = request.env.ref('sale.action_report_saleorder').sudo()._render_qweb_pdf([recod.id])
              data_record = base64.b64encode(pdf)
              ir_values = {
                    'name': 'Bon Commmande- '+ recod.name,
                    'type': 'binary',
                    'datas': data_record,
                    'store_fname': data_record,
                    'mimetype': 'application/pdf',
                    'res_model': 'vendeur.achat',
                         }
              report_commande = self.env['ir.attachment'].sudo().create(ir_values)
              ref_bl = self.env['stock.picking'].sudo().search([('group_id.sale_id.id', '=', recod.id)])
              recod.achat_vendeur.state = 'Devis Confirmer'
              pdf, _ = request.env.ref('stock.action_report_delivery').sudo()._render_qweb_pdf([ref_bl.id])
              data_record = base64.b64encode(pdf)
              ir_values = {
                    'name': 'Bon Livraison - '+ ref_bl.name,
                    'type': 'binary',
                    'datas': data_record,
                    'store_fname': data_record,
                    'mimetype': 'application/pdf',
                    'res_model': 'vendeur.achat',
                         }
              report_bl = self.env['ir.attachment'].sudo().create(ir_values)

              achat.sudo().message_post(body='Merci pour votre Commande', partner_ids=[2], attachment_ids=[report_commande.id,report_bl.id])
         return confirm

