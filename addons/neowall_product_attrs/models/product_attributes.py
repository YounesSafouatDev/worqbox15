from odoo import fields, models, api


class Marque(models.Model):
    _name = "neowall.marque"

    name = fields.Char(string="Nom")


class Format(models.Model):
    _name = "neowall.format"

    name = fields.Char(string="Nom")


class TypeGrammage(models.Model):
    _name = "neowall.typegrammage"

    name = fields.Char(string="Nom")


class Motif(models.Model):
    _name = "neowall.motif"

    name = fields.Char(string="Nom")


class Coloris(models.Model):
    _name = "neowall.coloris"

    name = fields.Char(string="Nom")

