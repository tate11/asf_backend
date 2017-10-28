# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class CondominiumDashboard(models.Model):
    _name = "condominium.dashboard"

    @api.one
    def _get_count(self):
        quotations_count = self.env['sale.order'].search(
            [('state', '=', 'draft')])
        orders_count = self.env['sale.order'].search(
            [('state', '=', 'sales_order')])
        orders_done_count = self.env['sale.order'].search(
            [('state', '=', 'done')])
 
        self.orders_count = len(orders_count)
        self.quotations_count = len(quotations_count)
        self.orders_done_count = len(orders_done_count)
 
    color = fields.Integer(string='Color Index')
    name = fields.Char(string="Name")
    orders_count = fields.Integer(compute = '_get_count')
    quotations_count = fields.Integer(compute= '_get_count')
    orders_done_count = fields.Integer(compute= '_get_count')

    # state = fields.Boolean('State')
    
    @api.one
    def dashboard_sales_action_id(self):
        print 'dashboard_sales_action_id'