# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Dashboard(models.Model):
    _name = "dashboard"

    @api.one
    def _get_count(self):
        quotations_count = self.env['sale.order'].search(
            [('sate', '=', 'draft')])
        orders_count = self.env['sale.order'].search(
            [('sate', '=', 'sales_order')])
        orders_done_count = self.env['sale.order'].search(
            [('sate', '=', 'done')])
 
        self.orders_count = len(orders_count)
        self.quotations_count = len(quotations_count)
        self.orders_done_count = len(orders_done_count)
 
    name = fields.Char(string="Name")
    
    company_id = fields.Many2one('res.company', string='Company',
                                 default=lambda self: self.env['res.company']._company_default_get('condominium.dashboard'))
    user_id = fields.Many2one('res.users', string='Team Leader')
    member_ids = fields.One2many('res.users', 'sale_team_id', string='Team Members')
    color = fields.Integer(string='Color Index')
    
    orders_count = fields.Integer(compute = '_get_count')
    quotations_count = fields.Integer(compute= '_get_count')
    orders_done_count = fields.Integer(compute= '_get_count')
        
    def dashboard_sales_action_id(self):
        print 'dashboard_sales_action_id'