from collections import defaultdict

from odoo import api, fields, models


class ligneVente(models.Model):
    _name = "vendeur.venteligne"
    _description = "vendeur gestion des lignes des ventes "

    product_id = fields.Many2one('product.product', string='Article')
    entetvente_id = fields.Many2one('vendeur.vente', string='Entet vente')
    quantity = fields.Integer(string='Quantité', default=1)
    total = fields.Float(string='MONTANT', compute='_def_calculer_total')
    prix = fields.Float(string='Prix Unitaire', related='product_id.lst_price')
    remis = fields.Float(string='Remise')

    def _def_calculer_total(self):
        for line in self:
            line.total = (line.prix * line.quantity) - ((line.prix * line.quantity) * line.remis )

    @api.onchange('product_id', 'quantity', 'remis')
    def calculer_total(self):
        for line in self:
            line.total = (line.prix * line.quantity) - ((line.prix * line.quantity) * line.remis)
