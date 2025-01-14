from pyexpat import model
from odoo import models, fields

class PublicCategory(models.Model):
    _inherit = "product.public.category"
    
    video_ids = fields.One2many('product.public.category.video', 'category_id', string="Videos", copy=True)

    def _get_videos(self):
        lst = []
        for categ in self:
            lst = lst + list(categ.video_ids)
        return lst