from email.policy import default
from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    sale_uom_id = fields.Many2one(
        'uom.uom', 'Unité de mesure de vente', required=False
    )
    uom_category_id = fields.Many2one(
        "uom.category", related="uom_id.category_id", string="Catégory d'UDM"
    )

    @api.onchange("uom_id")
    def remove_sale_uom(self):
        for rec in self:
            rec.sale_uom_id = False

    def get_sale_uom(self):
        for p in self:
            if not p.sale_uom_id:
                return p.uom_id
            return p.sale_uom_id.id
