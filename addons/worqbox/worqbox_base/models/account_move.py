# Copyright 2020 ForgeFlow S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    total_in_words = fields.Char(
        string="Total in Words",
        store=True,
        compute='_compute_check_total_in_words',
    )

    @api.depends('currency_id', 'amount_total')
    def _compute_check_total_in_words(self):
        for facture in self:
            if facture.currency_id:
                facture.total_in_words = facture.currency_id.amount_to_text(facture.amount_total)
            else:
                facture.total_in_words = False


