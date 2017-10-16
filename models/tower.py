# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Tower(models.Model):
    _name = 'condominium.tower'

    name = fields.Char(string='Torre', required=True)