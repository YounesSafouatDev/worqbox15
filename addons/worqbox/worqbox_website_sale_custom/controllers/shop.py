
from odoo.http import request
from odoo import http, tools
from odoo.osv import expression

from odoo.addons.website_sale.controllers.main import WebsiteSale

def tofloat(val, default=0):
    try:
        val = float(val)
    except ValueError:
        val = default
    return val

class WorqboxWebsiteSale(WebsiteSale):

    def _get_search_domain(self, search, category, attrib_values, search_in_description=True):
        domain = super()._get_search_domain(search, category, attrib_values, search_in_description=search_in_description)
        domain = expression.AND([domain, [('is_published', '=', True), ('company_ids', 'in', request.website.company_id.id)]])
        return domain

    @http.route([])
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        flexible = request.httprequest.args.get('flexible', 'all')
        min_hauteur = request.httprequest.args.get('min_hauteur', 0, type=tofloat)
        max_hauteur = request.httprequest.args.get('max_hauteur', 0, type=tofloat)
        min_profondeur = request.httprequest.args.get('min_profondeur', 0, type=tofloat)
        max_profondeur = request.httprequest.args.get('max_profondeur', 0, type=tofloat)
        min_longueur = request.httprequest.args.get('min_longueur', 0, type=tofloat)
        max_longueur = request.httprequest.args.get('max_longueur', 0, type=tofloat)
        
        request.website = request.website.with_context(
            flexible=flexible,
            min_hauteur=min_hauteur, max_hauteur=max_hauteur,
            min_profondeur=min_profondeur, max_profondeur=max_profondeur,
            min_longueur=min_longueur, max_longueur=max_longueur
        )
        res = super(WorqboxWebsiteSale, self).shop(page, category, search, min_price, max_price, ppg, **post)
        
        filter_by_dimensions_enabled = request.website.is_view_active('worqbox_website_sale_custom.filter_products_dimensions')
        if filter_by_dimensions_enabled:
            Product = request.env['product.template'].with_context(bin_size=True)
            domain = self._get_search_domain(search, category, None)
            from_clause, where_clause, where_params = Product._where_calc(domain).get_sql()
            
            query = f"""
                SELECT COALESCE(MIN(hauteur), 0), COALESCE(MAX(hauteur), 0),
                  COALESCE(MIN(profondeur), 0), COALESCE(MAX(profondeur), 0),
                  COALESCE(MIN(longueur), 0), COALESCE(MAX(longueur), 0)
                  FROM {from_clause}
                 WHERE {where_clause}
            """
            request.env.cr.execute(query, where_params)
            avail_min_hauteur, avail_max_hauteur, \
            avail_min_profondeur, avail_max_profondeur, \
            avail_min_longueur, avail_max_longueur = request.env.cr.fetchone()

            if min_hauteur:
                min_hauteur = min_hauteur if min_hauteur <= avail_max_hauteur else avail_min_hauteur
            if max_hauteur:
                max_hauteur = max_hauteur if max_hauteur >= avail_min_hauteur else avail_max_hauteur
            
            if min_profondeur:
                min_profondeur = min_profondeur if min_profondeur <= avail_max_profondeur else avail_min_profondeur
            if max_profondeur:
                max_profondeur = max_profondeur if max_profondeur >= avail_min_profondeur else avail_max_profondeur
            
            if min_longueur:
                min_longueur = min_longueur if min_longueur <= avail_max_longueur else avail_min_longueur
            if max_longueur:
                max_longueur = max_longueur if max_longueur >= avail_min_longueur else avail_max_longueur

            res.qcontext.update({
                'min_hauteur': min_hauteur or avail_min_hauteur,
                'max_hauteur': max_hauteur or avail_max_hauteur,
                'avail_min_hauteur': avail_min_hauteur,
                'avail_max_hauteur': avail_max_hauteur,
                'min_profondeur': min_profondeur or avail_min_profondeur,
                'max_profondeur': max_profondeur or avail_max_profondeur,
                'avail_min_profondeur': avail_min_profondeur,
                'avail_max_profondeur': avail_max_profondeur,
                'min_longueur': min_longueur or avail_min_longueur,
                'max_longueur': max_longueur or avail_max_longueur,
                'avail_min_longueur': avail_min_longueur,
                'avail_max_longueur': avail_max_longueur,
            })

        filter_by_flexible_enabled = request.website.is_view_active('worqbox_website_sale_custom.filter_products_flexible')
        if filter_by_flexible_enabled:
            res.qcontext.update({
                'flexible': flexible,
            })

        return res
