# -*- encoding: utf-8 -*-
from odoo import models, fields, api

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

    @api.multi
    def send_mail_template(self):
        # Find the e-mail template
        template = self.env.ref('openacademy.example_email_template')
        
        # You can also find the e-mail template like this:
        # template = self.env['ir.model.data'].get_object('mail_temppelate_demo', 'example_email_template')

        # Send out the e-mail template to the user
        self.env['mail.template'].browse(template.id).send_mail(self.id)

        # today_str = fields.Date.context_today()
        #
        # val1 = {'name': u'Eric Idle',
        #         'email': u'eric.idle@example.com'
        #                  'date': today_str}
        # val2 = {'name': u'John Cleese',
        #         'email': u'john.cleese@example.com',
        #         'date': today_str}
        #
        # partner_val = {
        #     'name': u'Flying Circus',
        #     'email': u'm.python@example.com',
        #     'date': today_str,
        #     'is_company': True,
        #     'child_ids': [(0, 0, val1),
        #                   (0, 0, val2),
        #                   ]
        # }