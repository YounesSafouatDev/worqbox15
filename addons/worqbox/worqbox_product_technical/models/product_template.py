from odoo import fields, models,api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # ORAC
    orac_technical_dwg = fields.Char('Modélisation dwg')
    orac_technical_max = fields.Char('Modélisation max')
  