# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    display_name = fields.Char('Full Name', compute='_compute_display_name', store=True)

    @api.depends('name', 'default_code')
    def _compute_field_name(self):
        for product in self:
            product.display_name = '[%s] %s' % (product.default_code, product.name)

    @api.model
    def _search_get_detail(self, website, order, options):
        res = super(ProductTemplate,self)._search_get_detail(website=website, order=order, options=options)
        
        res['fetch_fields'].append('display_name')
        
        res['mapping']['display_name'] = {'name': 'display_name', 'type': 'text', 'match': True}
        
        domains = res.get("base_domain")

        flexible = self.env.context.get('flexible', False)

        if flexible in ['flexible', 'no-flex']:
            if flexible == 'no-flex':
                domains.append([('orac_struct', '=', False)])
            else:
                domains.append([('orac_struct', '=', True)])
            res.update({"base_domain": domains})

        if self.env.context.get('min_hauteur', 0):
            domains.append([('hauteur', '>=', self.env.context.get('min_hauteur', 0))])
            res.update({"base_domain": domains})
        if self.env.context.get('max_hauteur', 0):
            domains.append([('hauteur', '<=', self.env.context.get('max_hauteur', 0))])
            res.update({"base_domain": domains})
        if self.env.context.get('min_profondeur', 0):
            domains.append([('profondeur', '>=', self.env.context.get('min_profondeur', 0))])
            res.update({"base_domain": domains})
        if self.env.context.get('max_profondeur', 0):
            domains.append([('profondeur', '<=', self.env.context.get('max_profondeur', 0))])
            res.update({"base_domain": domains})
        if self.env.context.get('min_longueur', 0):
            domains.append([('longueur', '>=', self.env.context.get('min_longueur', 0))])
            res.update({"base_domain": domains})
        if self.env.context.get('max_longueur', 0):
            domains.append([('longueur', '<=', self.env.context.get('max_longueur', 0))])
            res.update({"base_domain": domains})

        return res
