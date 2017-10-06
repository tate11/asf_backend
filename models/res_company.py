# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class Company(models.Model):
    _inherit = 'res.company'

    bank_name = fields.Char('Bank name')
    bank_account = fields.Char('Bank account')
    bank_owner = fields.Char('Bank owner')