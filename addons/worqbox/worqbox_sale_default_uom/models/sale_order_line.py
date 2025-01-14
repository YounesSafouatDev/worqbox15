from email.policy import default
from odoo import fields, models,api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange("product_id")
    def product_id_change(self):
        res = super(SaleOrderLine, self).product_id_change()
        for rec in self:
            if rec.product_template_id:
                rec.product_uom = rec.product_template_id.get_sale_uom()
        return res