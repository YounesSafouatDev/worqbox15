# -*- coding: utf-8 -*-

from odoo import models, fields


class Website(models.Model):
    _inherit = "website"

    def _default_social_tiktok(self):
        return self.env.ref('base.main_company').social_tiktok

    social_tiktok = fields.Char('Compte TikTok', default=_default_social_tiktok)
