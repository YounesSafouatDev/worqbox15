from odoo import fields, models,api


class ProductTemplate(models.Model):
    _inherit = "product.template"

    # ORAC
    orac_struct = fields.Boolean('Flexible')
    orac_struct_other = fields.Many2one('product.template', string="Article connexe")
    orac_company = fields.Boolean(string="Société ORAC", compute="_compute_companies", store=False)
    orac_technical_doc = fields.Char('Fiche technique')
    orac_scheme_url = fields.Char('Url schema')

    def action_generate_orac_name(self):
        if self.family.name:
            name = "%s - %s" % (self.family.name, self.categ_id.name)
        else:
            name = " - %s" % (self.categ_id.name)
        if self.orac_struct:
            name = name + " Flexible"
        self.write({'name': name})

    # def name_get(self):
    #     # Prefetch the fields used by the `name_get`, so `browse` doesn't fetch other fields
    #     self.browse(self.ids).read(['name'])
    #     return [(template.id, '%s' % (template.name))
    #             for template in self]

    # Company boolean
    @api.depends('company_ids')
    def _compute_companies(self):
        for rec in self:
            rec.orac_company = self.env.ref('base.orac_company') in rec.company_ids

    # General fields
    # default_code = fields.Char(required=True)
    family = fields.Many2one('worqbox.family', string='Famille')
