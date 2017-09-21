# -*- encoding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string="Distribución", required=True)

    asf_distribution = fields.Selection([('percent', 'Por % de participación'),('owner','Por propietario')])

