# -*- encoding: utf-8 -*-
from odoo import models, fields, api

class res_sales_order(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def create_order(self):
        vals = {
            'name': self.name,
            'state': 'invoice_exept',
            # 'date_order': self.date_order,
            # 'date_create': self.date_order,
            # 'date_confirm': self.date_confirm,
            # 'user_id': self.user_id.id,
            # 'partner_id': self.partner_id.id,
            'order_policy': 'manual'
        }

        # res = self.env['sale.order'].create(vals)
        # return res
