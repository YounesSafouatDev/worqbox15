from odoo.http import request
from odoo import api, fields, models, modules


class Users(models.Model):
    _inherit = "res.users"

    brand_ids = fields.Many2many(string="Brand", comodel_name="res.brand")

    @api.model_create_multi
    def create(self, vals_list):
        self.clear_caches()
        print("vals_list",vals_list)
        return super(Users, self).create(vals_list)

    def write(self, vals):
        if 'brand_ids' in vals:
            self.clear_caches()
        return super(Users, self).write(vals)

    def unlink(self):
        self.clear_caches()
        return super(Users, self).unlink()

