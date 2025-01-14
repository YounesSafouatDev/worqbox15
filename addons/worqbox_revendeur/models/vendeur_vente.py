# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from collections import defaultdict

from odoo import api, fields, models


class Vente(models.Model):
    _name = "vendeur.vente"
    _inherit = ['mail.thread']
    _description = "Devis Vente"

    client_id = fields.Many2one('res.partner', string='Client')
    achat_id = fields.Many2one('vendeur.achat', string='Devis Achat')
    client_adress = fields.Char(related='client_id.street')
    name = fields.Char(string='Devis name', compute='_compute_rename_vente')
    devis_date = fields.Date(string='Devis date', default=fields.Datetime.now)
    vente_linge = fields.One2many('vendeur.venteligne', 'entetvente_id', string='Articles')
    state = fields.Selection([('Devis', 'Devis'),
                              ('Commande', 'Commande'),
                              ('Facteur', 'Facteur')
                              ], default='Devis', string='Statue')
    totalht = fields.Float(string='Montant HT', compute='_reclcaler_totalht')
    totaltva = fields.Float(string='TVA 20%', compute='_reclcaler_totaltva')
    total = fields.Float(string='Total TTC', compute='_reclcaler_totalttc')
    marge = fields.Float(string='Marge', compute='_reclcaler_marge')
    vendeur = fields.Many2one('res.users', string='Vendeur', default=lambda self: self.env.user)

    def _compute_rename_vente(self):
        for rec in self:
            rec.write({'name': 'Devis N° V' + str(rec.id)})

    @api.onchange('vente_linge', 'vente_linge.total')
    def _reclcaler_marge(self):
        total = 0
        for record in self:
            for line in record.vente_linge:
                if line.product_id.categ_id.id != 305:
                    total += (line.quantity * line.prix) * (int(record.vendeur.partner_id.x_studio_remis_revtement_) / 100)
                else:
                    total += (line.quantity * line.prix) * (int(record.vendeur.partner_id.x_studio_remise_consommable_) / 100)
            record.write({'marge': total})

    @api.onchange('vente_linge', 'vente_linge.total')
    def _reclcaler_totalht(self):
        total = 0
        for record in self:
            for line in record.vente_linge:
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




