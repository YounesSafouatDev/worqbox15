from odoo import fields, models, api


class LplCollection(models.Model):
    _name = "orac.lplcollect"

    name = fields.Char(string="Nom")


class Compostion(models.Model):
    _name = "orac.composition"

    name = fields.Char(string="Nom")


class EssenceBois(models.Model):
    _name = "orac.woodessence"

    name = fields.Char(string="Nom")


class WoodChoise(models.Model):
    _name = "orac.woodchoise"

    name = fields.Char(string="Nom")


class Format(models.Model):
    _name = "orac.format"

    name = fields.Char(string="Nom")


class UsageClassification(models.Model):
    _name = "orac.usageclassification"

    name = fields.Char(string="Nom")


class IntegratedUnderlay(models.Model):
    _name = "orac.integratedunderlay"

    name = fields.Char(string="Nom")


class Chamfer(models.Model):
    _name = "orac.chamfer"

    name = fields.Char(string="Nom")


class Instalation(models.Model):
    _name = "orac.installation"

    name = fields.Char(string="Nom")


class Finition(models.Model):
    _name = "orac.finition"

    name = fields.Char(string="Nom")


class Protection(models.Model):
    _name = "orac.protection"

    name = fields.Char(string="Nom")


class Guarantee(models.Model):
    _name = "orac.guarantee"

    name = fields.Char(string="Nom")
