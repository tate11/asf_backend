from odoo import api, fields, model

class WizardGenerateSaleOrder(model.TransientModel):
    _name = "wizard.generate.sale.order"
    _description = "Generar ordenes de pago"

    title = fields.Char('Title', required=True)

    @api.multi
    def action_wizard_generate_sale_order(self):
        print 'action generate!!!'
        print 'action generate 2222!!!'
        return True