# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CondominiumConfigSettings(models.TransientModel):

    _name = 'condominium.config.settings'
    _inherit = 'sale.config.settings'

    water_default_item = fields.Many2one('product.template',
        ondelete='cascade', string="Item")
    
    deposit_product_id_settings = fields.Many2one(
        'product.template',
        'Deposit Product',
        # domain="[('type', '=', 'service')]",
        help='Default product used for payment advances', 
        required=True)
    
    # @api.multi
    # def set_deposit_product_id_defaults(self):
    #     return self.env['ir.values'].sudo().set_default(
    #         'sale.config.settings', 'deposit_product_id_settings', self.deposit_product_id_settings.id)
