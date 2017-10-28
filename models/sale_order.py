# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_maintenance_fee = fields.Boolean(string="Es mantenimiento")
    period = fields.Many2one('condominium.period',
        ondelete='cascade', string="Período")

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

        # tax_ids = self._get_taxes_invoice(cursor, user, move_line, type)

        for customer in customers:

            new_order = {
                'user_id': self.user_id.id,
                'partner_id': customer.id,
                'validity_date': self.validity_date,
                'payment_term_id': self.payment_term_id.id, # template_order.payment_term_id.id
                'note': self.note,
                'is_maintenance_fee': True,
                'period': self.period.id
            }

            percent = 0
            for ownership in customer.ownership_id:
                percent = percent + ownership.asf_percent

            order = self.env['sale.order'].create(new_order)
            amount = 0

            for template_order_item in template_order_items:
                product = self.env['product.template'].search([('id', '=', template_order_item.product_id.id)])

                # taxes = template_order_item.product_id.taxes_id.filtered(lambda r: not order.company_id or r.company_id == order.company_id)

                order_line = order.order_line.filtered(lambda line: line.product_id == template_order_item.product_id.id)
                if order_line:
                    order_line[0].product_uom_qty += 1
                else:
                    if template_order_item.distribution == 'owner':
                        amount = template_order_item.price_unit / len(customers)
                    elif template_order_item.distribution == 'percent':
                        # amount = template_order_item.price_unit * customer.percent / 100
                        amount = template_order_item.price_unit * percent / 100
                    else:
                        amount = template_order_item.price_unit

                    water_default_item = self.env['condominium.water_default_item'].search([('name', '=', template_order_item.name)])
                    if len(water_default_item):
                        print(len(water_default_item))

                        amount = template_order_item.price_unit
                        
                        water_counter = self.env['condominium.water_counter'].search(
                            [('name', '=', customer.id),('period','=',self.period.id)])

                        if len(water_counter):
                            total = water_counter.current - water_counter.old
                            template_order_item.product_uom_qty = total
                            # amount = template_order_item.price_unit

                    else:
                        print('else len')

                    # tax_ids = taxes.ids
                    new_item = {
                        'order_id': order.id,
                        'product_id': template_order_item.product_id.id,
                        'product_uom_qty': template_order_item.product_uom_qty,
                        'distribution': template_order_item.distribution,
                        'price_unit': amount,
                        # 'tax_id': [(6, 0, tax_ids)],
                    }

                    order_line = self.env['sale.order.line'].create(new_item)
                    order_line._compute_tax_id()
                    # product_id_change()

            # water_counter_items = self.env['condominium.water_default_item'].search([('name', '=', self.id)])
            # for water_counter_item in water_counter_items:

                    
        return super(SaleOrder, self).action_cancel()

# product_uom_change()
# _compute_invoice_status()
# _compute_amount()
# _get_to_invoice_qty()
# _get_price_reduce()

        # self.write({'line_id': order_line.id})
        # return {'type': 'ir.actions.client', 'tag': 'reload'}

