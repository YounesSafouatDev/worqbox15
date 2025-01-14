# -*- coding: utf-8 -*-
from odoo import models, fields

class CrmStage(models.Model):
    _inherit = ["multi.company.abstract", "crm.stage"]
    _name = "crm.stage"
