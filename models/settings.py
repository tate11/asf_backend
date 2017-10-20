# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Settins(models.Model):
    _name = 'condominium.settings'

    name = fields.Char("Demo")

    # name = fields.Many2one('res.partner',
    #     ondelete='cascade', string="Propietario", required=True)
    # period = fields.Many2one('condominium.period',
    #     ondelete='cascade', string="Período", required=True)
    # old = fields.Float(string='Contador anterior', required=True)
    # current = fields.Float(string='Contador actual', required=True)
    # date = fields.Date(string="Fecha", required=True)