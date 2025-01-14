from odoo import fields, models,api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    profondeur = fields.Float(string="Profondeur (cm)")
    hauteur = fields.Float(string="Hauteur (cm)")
    longueur = fields.Float(string="Longueur (cm)")
    diametre = fields.Float(string="Diamètre (cm)")

    @api.onchange("profondeur","hauteur","longueur","diametre")
    def onchange_description(self):
        if self.product_brand_id:
            description = ''
            if self.profondeur:
                description += '\n' + "Profondeur : " + str(self.profondeur) + ' cm'
            if self.hauteur:
                description += '\n' +"Hauteur : " + str(self.hauteur) + ' cm'
            if self.longueur:
                description += '\n' + "Longueur : " + str(self.longueur) + ' cm'
            if self.diametre:
                description += '\n' + "Diametre : " + str(self.diametre) + ' cm'
            self.description_sale = description

   # sales_count = fields.Float(store=True)
    qty_available = fields.Float(store=True)
    virtual_available = fields.Float(store=True)
    stock_value = fields.Float(compute='_compute_stock_value', string='Stock Value')
    
    @api.depends('qty_available', 'standard_price')
    def _compute_stock_value(self):
        for rec in self:
            rec.stock_value = rec.qty_available * rec.standard_price
