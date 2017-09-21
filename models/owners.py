# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Owners(models.Model):
    _name = 'openacademy.owner'

    name = fields.Char(string='Nombres', required=True)
    doi = fields.Char(string='Documento de identidad', required=True)
    email = fields.Char(string='Correo electrónico', required=True)
    cellphone = fields.Char(string='Celular', required=True)
    job = fields.Char(string='Ocupación')