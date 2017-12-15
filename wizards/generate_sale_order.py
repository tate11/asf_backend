# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class WizardGenerateSaleOrder(models.TransientModel):
    _name = "wizard.generate.sale.order"
    _description = "Generar ordenes de pago"

    title = fields.Char('Title', required=True)
    field_One2many = fields.Many2one('sale.order.line',
        ondelete='set null', string="Order line", index=True)
        
    attendee_ids = fields.Many2one('sale.order.line',
        ondelete='set null', string="Order line", index=True)


    @api.multi
    def action_wizard_generate_sale_order(self):
        print('action generate!!!')
        print('action generate 2222!!!')
        return True

# from openerp import fields,models
class sale_order(models.Model):
     _inherit='sale.order'
    #  field_One2many=fields.One2many('sale.order.line','order_id','Order')

     field_One2many = fields.Many2one('sale.order.line',
        ondelete='set null', string="Order line", index=True)

# sale_order()

class sale_order_line(models.model):
     _inherit='sale.order.line'
     order_id=fields.Many2one('wizard.generate.sale.order','Order')
# sale_order_line()