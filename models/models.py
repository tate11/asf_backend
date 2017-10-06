# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class GenearteSaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def action_generate_sale_order(self):

        self.ensure_one()

        if self.state not in ['draft']:
            return False

        customers = self.env['res.partner'].search([('is_owner', '=', True)])
        template_order = self.env['sale.order']
        template_order_items = self.env['sale.order.line'].search([('order_id', '=', self.id)])

        for customer in customers:

            new_order = {
                'user_id': self.user_id.id,
                'partner_id': customer.id,
                'validity_date': self.validity_date,
                'payment_term_id': self.payment_term_id.id, # template_order.payment_term_id.id
                'note': self.note,
            }

            order = self.env['sale.order'].create(new_order)
            amount = 0

            for template_order_item in template_order_items:
                product = self.env['product.template'].search([('id', '=', template_order_item.product_id.id)])

                order_line = order.order_line.filtered(lambda line: line.product_id == template_order_item.product_id.id)
                if order_line:
                    order_line[0].product_uom_qty += 1
                else:
                    if template_order_item.distribution == 'owner':
                        amount = template_order_item.price_unit / len(customers)
                    else:
                        amount = template_order_item.price_unit * customer.percent / 100

                    new_item = {
                        'order_id': order.id,
                        'product_id': template_order_item.product_id.id,
                        'product_uom_qty': template_order_item.product_uom_qty,
                        'distribution': template_order_item.distribution,
                        'price_unit': amount,
                    }

                    order_line = self.env['sale.order.line'].create(new_item)
                    order_line._compute_tax_id()