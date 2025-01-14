# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError
from odoo.addons.website.tools import get_video_embed_code

import re
import base64
import json
import requests

ytRegex = r'^(?:(?:https?:)?\/\/)?(?:www\.)?(?:youtu\.be\/|youtube(-nocookie)?\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((?:\w|-){11})(?:\S+)?$'
vimeoRegex = r'\/\/(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*'

class CategoryVideo(models.Model):
    _name = 'product.public.category.video'
    _description = "Category Video"
    _inherit = ['image.mixin']
    _order = 'sequence, id'

    name = fields.Char("Name", required=True)
    sequence = fields.Integer(default=10, index=True)

    thumbnail = fields.Image(required=True)

    category_id = fields.Many2one('product.public.category', "Product Category", index=True, ondelete='cascade')
    video_url = fields.Char('Video URL',
                            help='URL of a video for showcasing your product.')
    embed_code = fields.Html(compute="_compute_embed_code", sanitize=False)

    @api.depends('video_url')
    def _compute_embed_code(self):
        for image in self:
            image.embed_code = get_video_embed_code(image.video_url)

    @api.constrains('video_url')
    def _check_valid_video_url(self):
        for image in self:
            if image.video_url and not image.embed_code:
                raise ValidationError(_("Provided video URL for '%s' is not valid. Please enter a valid video URL.", image.name))

    @api.onchange('video_url')
    def _get_youtube_thumbnail(self):
        if not self.video_url:
            return

        ytMatch = re.search(ytRegex, self.video_url)
        if ytMatch and len(ytMatch.groups()[1]) == 11:
            thumbUrl = "https://img.youtube.com/vi/%s/0.jpg" % ytMatch.groups()[1]
            content = requests.get(thumbUrl).content
            self.thumbnail = base64.b64encode(content).replace(b'\n', b'')
            return

        vimeoMatch = re.search(vimeoRegex, self.video_url)
        if vimeoMatch:
            jsonUrl = "https://vimeo.com/api/oembed.json?url=https://vimeo.com/%s" % vimeoMatch.groups()[2]
            jsonFile = requests.get(jsonUrl).content
            jsonFile = json.loads(jsonFile)
            self.thumbnail = base64.b64encode(requests.get(jsonFile["thumbnail_url_with_play_button"]).content).replace(b'\n', b'')
