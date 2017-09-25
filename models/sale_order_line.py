# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    distribution = fields.Selection([('percent', 'Por % de participación'),('owner','Por propietario')])
