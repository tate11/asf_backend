# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Period(models.Model):
    _name = 'condominium.period'

    name = fields.Char(string='Período', required=True)