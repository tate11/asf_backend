# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class WaterDefaultItem(models.Model):
    _name = 'condominium.water_default_item'

    name = fields.Many2one('product.template',
        ondelete='cascade', string="Item", required=True)