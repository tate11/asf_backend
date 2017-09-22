# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string="Distribución", required=True)

    asf_distribution = fields.Selection([('percent', 'Por % de participación'),('owner','Por propietario')])
    # asf_type = fields.Selection([('apartment','Departamento'),('depot','Deposito'),('parking','Estacionamiento')])

    type = fields.Selection(selection_add=[('apartment','Departamento'),('depot','Depósito'),('parking','Estacionamiento')])

class Partner(models.Model):
    # _name = 'openacademy.partner'
    _inherit = 'res.partner'

    name = fields.Char(required=True)
    is_owner = fields.Boolean(string='Is owner')
    
    apartment_id = fields.Many2many('openacademy.apartment', string="Apartments")
    percent = fields.Float(required=True)

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


class res_partner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def create_sale(self):
        self.ensure_one()
        # slips = self.env['hr.payslip'].search([])
        # # Exception because you cannot access the field directly on multi entries
        # print slips.id
        # # Working
        # print slips.ids
        # for slip in slips:
        #     print slip.id
        #

        # customers = self.env['res.partner'].search([])
        # self.env['res.users'].search([('login', '=', 'admin')])
        customers = self.env['res.partner'].search([('is_owner', '=', True)])
        # line_env = self.env['sale.order.line']

        for customer in customers:
            customer_id = customer.id;

            line_1 = {
                'product_id': 1,
                # 'name': 'Product name',
                'product_uom_qty': 1,
                'price_unit': 10
            }

            # document_val = {
            #     'partner_id': customer_id,
            #     'child_ids': [(0, 0, line_1)],
            # }

            document_val = {
                # 'name': self.name,
                # 'state': 'sale',
                # 'date_order': self.date_order,
                # 'date_create': self.date_order,
                # 'date_confirm': self.date_confirm,
                'user_id': self.user_id,
                'partner_id': customer_id,
                # 'order_policy': 'manual'
            }

            order = self.env['sale.order'].create(document_val)

            vals = {
                'price_unit': 10,
                # 'website_description': self.website_description,
                # 'name': self.name,
                'order_id': order.id,
                'product_id': 1,
                # 'layout_category_id': self.layout_category_id.id,
                'product_uom_qty': 1,
            }
            order_line = self.env['sale.order.line'].create(vals)
            order_line._compute_tax_id()

            vals2 = {
                'price_unit': 20,
                # 'website_description': self.website_description,
                # 'name': self.name,
                'order_id': order.id,
                'product_id': 1,
                # 'layout_category_id': self.layout_category_id.id,
                'product_uom_qty': 1,
            }
            order_line = self.env['sale.order.line'].create(vals2)
            order_line._compute_tax_id()

            vals3 = {
                'price_unit': 30,
                # 'website_description': self.website_description,
                # 'name': self.name,
                'order_id': order.id,
                'product_id': 1,
                # 'layout_category_id': self.layout_category_id.id,
                'product_uom_qty': 1,
            }
            order_line = self.env['sale.order.line'].create(vals3)
            order_line._compute_tax_id()



        # return record

    @api.multi
    def read_partners(self):
        # partners = self.env['res.partner']

        sql = ('SELECT country_id, array_agg(id) '
               'FROM res_partner '
               'WHERE active=true AND is_owner=true '
               'GROUP BY country_id')
        self.env.cr.execute(sql)

        country_model = self.env['res.country']
        result = {}
        for country_id, partner_ids in self.env.cr.fetchall():
            country = country_model.browse(country_id)

            print  country.name
        #     partners = self.search(
        #         [('id', 'in', tuple(partner_ids))]
        #     )
        # result[country] = partners
        # return result

    @api.multi
    def create_partner(self):

        # today_str = fields.Date.context_today()
        partner_val = {
            'name': u'Flying Circus',
            'email': u'm.python@example.com',
            'is_owner': True,
            'percent': u'3',
            # 'date': today_str,
            'is_company': True
        }

        record = self.env['res.partner'].create(partner_val)

        return record
