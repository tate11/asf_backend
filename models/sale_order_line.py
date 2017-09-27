# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    distribution = fields.Selection([('percent', 'Por % de participación'),('owner','Por propietario')])

    @api.onchange('distribution')
    def _onchange_distribution(self):
        self.description = self.product_id.description_sale # Fill description box from description_sale
        self.price = self.product_id.lst_price # Fill price box with default product price
        self.tax_id = self.product_id.taxes_id # Fill tax box with default tax (many2many)
