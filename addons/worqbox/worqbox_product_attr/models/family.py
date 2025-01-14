from odoo import fields, models,api

class family(models.Model):
    _name = 'worqbox.family'
    _description = 'Famille de l\'article'

    name = fields.Char('Nom de la famille')
    company_id = fields.Many2one('res.company', 'Société', required=True,
        default=lambda self: self.env.company, index=1)
    