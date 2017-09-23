# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # @api.multi
    # def button_add_to_order(self):
    #     self.ensure_one()
    #     order = self.order_id
    #     if order.state not in ['draft', 'sent']:
    #         return False
    #
    #     order_line = order.order_line.filtered(lambda line: line.product_id == self.product_id)
    #     if order_line:
    #         order_line[0].product_uom_qty += 1
    #     else:
    #         vals = {
    #             'price_unit': self.price_unit,
    #             'website_description': self.website_description,
    #             'name': self.name,
    #             'order_id': order.id,
    #             'product_id': self.product_id.id,
    #             'layout_category_id': self.layout_category_id.id,
    #             'product_uom_qty': self.quantity,
    #             'product_uom': self.uom_id.id,
    #             'discount': self.discount,
    #         }
    #         order_line = self.env['sale.order.line'].create(vals)
    #         order_line._compute_tax_id()
    #
    #     self.write({'line_id': order_line.id})
    #     return {'type': 'ir.actions.client', 'tag': 'reload'}

    @api.multi
    def create_orders(self):
        self.ensure_one()

        # order = self.id
        if self.state not in ['draft']:
            return False

        customers = self.env['res.partner'].search([('is_owner', '=', True)])
        template_order = self.env['sale.order']
        # template_order_items = self.env['sale.order.line'].search('order_id', '=', template_order.id)
        template_order_items = self.env['sale.order.line'].search([('order_id', '=', self.id)])

        for customer in customers:

            new_order = {
                'user_id': self.user_id.id,
                'partner_id': customer.id,
                # 'payment_term_id': self.payment_term_id
            }

            order = self.env['sale.order'].create(new_order)
            amount = 0

            for template_order_item in template_order_items:
                product = self.env['product.template'].search([('id', '=', template_order_item.product_id.id)])
                order_line = order.order_line.filtered(lambda line: line.product_id == template_order_item.product_id.id)
                if order_line:
                    order_line[0].product_uom_qty += 1
                else:
                    if product.asf_distribution == 'owner':
                        amount = template_order_item.price_unit / len(customers)
                    else:
                        amount = template_order_item.price_unit * customer.percent / 100

                    new_item = {
                        'order_id': order.id,
                        'product_id': template_order_item.product_id.id,
                        'product_uom_qty': template_order_item.product_uom_qty,
                        # 'price_unit': template_order_item.price_unit
                        'price_unit': amount
                    }

                    order_line = self.env['sale.order.line'].create(new_item)
                    order_line._compute_tax_id()
                    # product_id_change()
# product_uom_change()
# _compute_invoice_status()
# _compute_amount()
# _get_to_invoice_qty()
# _get_price_reduce()

        # self.write({'line_id': order_line.id})
        # return {'type': 'ir.actions.client', 'tag': 'reload'}

