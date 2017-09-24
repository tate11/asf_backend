# -*- encoding: utf-8 -*-

from odoo import api, fields, models

class WizardGenerateSaleOrder(models.TransientModel):
    _name = "wizard.generate.sale.order"
    _description = "Generar ordenes de pago"

    title = fields.Char('Title', required=True)

    @api.multi
    def action_wizard_generate_sale_order(self):
        print 'action generate!!!'
        print 'action generate 2222!!!'
        return True