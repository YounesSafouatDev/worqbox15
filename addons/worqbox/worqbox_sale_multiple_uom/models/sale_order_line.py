from email.policy import default
from odoo import fields, models,api

from odoo.tools import float_round

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange("product_uom", "product_uom_qty")
    def onchange_product_uom(self):
        for line in self:
            default_uom = line.product_id.uom_id
            if default_uom == line.product_uom:
                return

            mul_qty = line.product_uom._compute_quantity(line.product_uom_qty, default_uom)
            mul_qty_rounded = float_round(mul_qty, precision_rounding=1.0, rounding_method="UP")
            line.product_uom_qty = default_uom._compute_quantity(mul_qty_rounded, line.product_uom)







