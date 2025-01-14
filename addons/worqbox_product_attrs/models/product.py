from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # ORAC_new_fields
    lpl_collection = fields.Many2one('orac.lplcollect', string="Collection LPL")

    composition = fields.Many2one('orac.composition', string="Composition")
    essence_bois = fields.Many2one('orac.woodessence', string="Essence de bois")
    wood_choice = fields.Many2one('orac.woodchoise', string="Choix de bois")
    format = fields.Many2one('orac.format', string="Format")
    usage_classification = fields.Many2one('orac.usageclassification', string="Classement usage")
    guarantee = fields.Many2one('orac.guarantee', string="Garantie")
    water_resistance = fields.Selection([
        ('Hydroseal', 'Hydroseal'),

    ], string="Résistance à l'eau", default="")

    scratch_resistance = fields.Selection([

        ('Scratch guard', 'Scratch guard'),

    ], string="Résitance aux rayures", default="")

    thickness = fields.Integer(string="Épaisseur (mm)")
    parement = fields.Integer(string="Parement (mm)")
    depth = fields.Integer(string="Profondeur (mm)")
    width = fields.Float(string="Largeur (mm)", digits='Product Price',)
    hight = fields.Integer(string="Hauteur (mm)")
    length = fields.Float(string="Longueur (mm)", digits='Product Price',)
    diameter = fields.Integer(string="Diamètre (mm)")

    integrated_underlay = fields.Many2one('orac.integratedunderlay', string="Sous couche intégrée")
    chamfer = fields.Many2one('orac.chamfer', string="Chanfrein")
    installation = fields.Many2one('orac.installation', string="Installation")
    finition = fields.Many2one('orac.finition', string="Finition")
    protection = fields.Many2one('orac.protection', string="Protection")
    margin = fields.Float(compute="_get_sale_amounts", string="Marge HT / m2, ml ou pièce", digits='Product Price', )
    margin_percent = fields.Float(compute="_get_sale_amounts", string="")
    sale_price_unit = fields.Float(compute="_get_sale_amounts", string="Prix de vente TTC / m2, ml ou pièce",
                                   digits='Product Price')
    cost_price_unit = fields.Float(compute="_get_sale_amounts", string="Coût TTC / m2, ml ou pièce",
                                   digits='Product Price', )
    main_seller_id = fields.Many2one(comodel_name="res.partner", compute="_get_main_seller", string="Fournisseur")

    def _get_sale_amounts(self):
        for record in self:
            record.sale_price_unit = record.list_price * 1.2 / (record.uom_id.factor_inv if record.uom_id.factor_inv else 1)
            record.cost_price_unit = record.standard_price * 1.2 / (record.uom_id.factor_inv if record.uom_id.factor_inv else 1)
            record.margin = (record.sale_price_unit - record.cost_price_unit) / 1.2
            record.margin_percent = (record.margin / ((record.cost_price_unit if record.cost_price_unit else 1) / 1.2)) * 100

    @api.depends('seller_ids')
    def _get_main_seller(self):
        for record in self:
            if record.seller_ids:
                record.main_seller_id = record.seller_ids[0].name.id
            else:
                record.main_seller_id = None

    @api.onchange("lpl_collection", "composition", "essence_bois", "wood_choice", "format", "usage_classification",
                  "water_resistance", "scratch_resistance", "thickness", "parement", "depth",
                  "width", "hight", "length", "diameter", "integrated_underlay", "chamfer", "installation", "finition",
                  "protection")
    def onchange_description(self):
        if self.company_id.id == 1 or self.company_id.id == 11:
            description = ''
            if self.lpl_collection:
                description += '\n' + "Collection LPL : " + str(self.lpl_collection.name)

            if self.composition:
                description += '\n' + "Composition : " + str(self.composition.name)

            if self.essence_bois:
                description += '\n' + "Essence de bois : " + str(self.essence_bois.name)

            if self.wood_choice:
                description += '\n' + "Choix de bois : " + str(self.wood_choice.name)

            if self.format:
                description += '\n' + "Format : " + str(self.format.name)

            if self.usage_classification:
                description += '\n' + "Classement usage : " + str(self.usage_classification.name)

            if self.water_resistance:
                description += '\n' + "Résistance à l'eau : " + str(self.water_resistance)

            if self.scratch_resistance:
                description += '\n' + "Résitance aux rayures: " + str(self.scratch_resistance)

            if self.thickness:
                description += '\n' + "Épaisseur : " + str(self.thickness) + ' mm'

            if self.parement:
                description += '\n' + "Parement : " + str(self.parement) + ' mm'

            if self.depth:
                description += '\n' + "Profondeur : " + f"{self.depth:,.2f}".replace(',', ' ').replace('.',
                                                                                                       ',') + ' mm'  # Already exists
            if self.width:
                description += '\n' + "Largeur : " + f"{self.width:,.2f}".replace(',', ' ').replace('.', ',') + ' mm'

            if self.hight:
                description += '\n' + "Hauteur : " + f"{self.hight:,.2f}".replace(',', ' ').replace('.',
                                                                                                    ',') + ' mm'  # Already exists

            if self.length:
                description += '\n' + "Longueur : " + f"{self.length:,.2f}".replace(',', ' ').replace('.',
                                                                                                      ',') + ' mm'  # Already exists

            if self.diameter:
                description += '\n' + "Diamètre : " + f"{self.diameter:,.2f}".replace(',', ' ').replace('.',
                                                                                                        ',') + ' mm'  # Already exists

            if self.integrated_underlay:
                description += '\n' + "Sous couche intégrée : " + str(self.integrated_underlay.name)

            if self.chamfer:
                description += '\n' + "Chanfrein : " + str(self.chamfer.name)

            if self.installation:
                description += '\n' + "Installation : " + str(self.installation.name)

            if self.finition:
                description += '\n' + "Finition : " + str(self.finition.name)

            if self.protection:
                description += '\n' + "Protection : " + str(self.protection.name)

            if self.guarantee:
                description += '\n' + "Garantie : " + str(self.guarantee.name)
            self.description_sale = description
