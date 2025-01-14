# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    social_tiktok = fields.Char(related='website_id.social_tiktok', readonly=False)

    @api.depends('website_id', 'social_twitter', 'social_facebook', 'social_github', 'social_linkedin',
                 'social_youtube', 'social_instagram', 'social_tiktok')
    def has_social_network(self):
        self.has_social_network = self.social_twitter or self.social_facebook or self.social_github \
                                  or self.social_linkedin or self.social_youtube or self.social_instagram \
                                  or self.social_tiktok

    def inverse_has_social_network(self):
        super(ResConfigSettings, self).inverse_has_social_network()
        if not self.has_social_network:
            self.social_tiktok = ''

    has_social_network = fields.Boolean("Configure Social Network", compute=has_social_network,
                                        inverse=inverse_has_social_network)
