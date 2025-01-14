
from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})

    products = env['product.template'].search([])
    products._compute_no_company_ids()

    partners = env['res.partner'].search([])
    partners._compute_no_company_ids()
