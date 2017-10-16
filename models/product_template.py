# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    name = fields.Char(string="Distribución", required=True)

    # asf_distribution = fields.Selection([('percent', 'Por % de participación'),('owner','Por propietario')])
    # asf_type = fields.Selection([('apartment','Departamento'),('depot','Deposito'),('parking','Estacionamiento')])

    type = fields.Selection(selection_add=[('apartment','Departamento'),('depot','Depósito'),('parking','Estacionamiento')])
    asf_percent = fields.Char(string="% de participación")
    asf_area = fields.Char(string="Área en m2")
    tower_id = fields.Many2one('condominium.tower',
        ondelete='cascade', string="Torre")

    floor_id = fields.Many2one('condominium.floor',
        ondelete='cascade', string="Piso")
