# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict
import base64
from odoo import api, fields, models
from odoo.http import request


class Achat(models.Model):
    _name = "vendeur.achat"
    _inherit = ['mail.thread']
    _description = "Devis achat"

    client_id = fields.Many2one('res.partner', string='Client', default=lambda self: self.env.user.partner_id.id)
    client_adress = fields.Char(related='client_id.street', default=lambda self: self.env.user.partner_id.street)
    name = fields.Char(string='Devis name', compute='_compute_rename_achat')
    or_mar_devis_id = fields.Many2one('sale.order', string='Devis Orac Maroc')
    devis_date = fields.Date(string='Devis date', default=fields.Datetime.now)
    achat_linge = fields.One2many('vendeur.achatligne', 'entetachat_id', string='Articles')
    totalht = fields.Float(string='Montant HT', compute='_reclcaler_totalht')
    totaltva = fields.Float(string='TVA 20%', compute='_reclcaler_totaltva')
    total = fields.Float(string='Total TTC', compute='_reclcaler_totalttc')
    state = fields.Selection([('Devis Non Envoyer', 'Devis Non Envoyer'),
                              ('Devis Envoyer', 'Devis Envoyer'),
                              ('Devis Confirmer', 'Devis Confirmer')
                              ], default='Devis Non Envoyer', string='Statue Devis Orac Maroc')

    def _compute_rename_achat(self):
        for rec in self:
            rec.write({'name': 'Devis N° A' + str(rec.id)})

    @api.onchange('achat_linge', 'achat_linge.total')
    def _reclcaler_totalht(self):
        total = 0
        for record in self:
            for line in record.achat_linge:
                total += line.total
            record.write({'totalht': total})

    @api.onchange('totalht')
    def _reclcaler_totaltva(self):
        for record in self:
            record.write({'totaltva': record.totalht * 0.2})

    @api.onchange('totaltva', 'totalht')
    def _reclcaler_totalttc(self):
        for record in self:
            record.write({'total': record.totalht + record.totaltva})

    def action_achat(self):
        for record in self:
            id_devis = self.env['sale.order'].sudo().create(
                {
                    'partner_id': record.client_id.id,
                    'date_order': record.devis_date,
                    'achat_vendeur': record.id
                }
            )
            record.update({'or_mar_devis_id': id_devis, 'state':'Devis Envoyer'})
            print(record.achat_linge)
            for line in record.achat_linge:
                record.env['sale.order.line'].sudo().create(
                    {
                        'product_id': line.product_id.id,
                        'product_uom_qty': line.quantity,
                        'order_id': id_devis.id,
                        'discount' : line.remis * 100

                    })
            

        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Votre commader a ete bien envoyer ',
                'type': 'rainbow_man',
            }
        }