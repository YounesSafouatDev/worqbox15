# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSale(WebsiteSale):

    def _get_mandatory_fields_billing(self, country_id=False):
        req = ["name", "phone","city"]
        return req

    def _get_mandatory_fields_shipping(self, country_id=False):
        req = ["name", "phone","city"]
        return req