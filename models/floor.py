# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Floor(models.Model):
    _name = 'condominium.floor'

    name = fields.Char(string='Piso', required=True)