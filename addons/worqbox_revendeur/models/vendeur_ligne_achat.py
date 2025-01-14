from collections import defaultdict

from odoo import api, fields, models


class ligneAchat(models.Model):
    _name = "vendeur.achatligne"
    _description = "vendeur gestion des lignes des achats "

    product_id = fields.Many2one('product.product', string='Article')
    entetachat_id = fields.Many2one('vendeur.achat', string='Entet achat')
    quantity = fields.Integer(string='Quantité', default=1)
    total = fields.Float(string='MONTANT', compute='_def_calculer_total')
    remis = fields.Float(string='Remis')
    prix = fields.Float(string='Prix Unitaire', related='product_id.lst_price')
    current_user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)

    def _def_calculer_total(self):
        for line in self:
            if line.product_id.categ_id.id != 305:
                line.write({'remis': (int(line.current_user.partner_id.x_studio_remis_revtement_) / 100)})
            else : 
                line.write({'remis': (int(line.current_user.partner_id.x_studio_remise_consommable_) / 100)})
            line.total = (line.prix * line.quantity) - (
                    line.prix * line.quantity * line.remis)

    @api.onchange('product_id', 'quantity')
    def calculer_total(self):
        for line in self:
             if line.product_id.categ_id.id != 305:
                line.write({'remis': (int(line.current_user.partner_id.x_studio_remis_revtement_) / 100)})
             else : 
                line.write({'remis': (int(line.current_user.partner_id.x_studio_remise_consommable_) / 100)})
             line.total = (line.prix * line.quantity) - (
                    line.prix * line.quantity * line.remis)
