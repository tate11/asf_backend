# -*- encoding: utf-8 -*-

from odoo import models, fields, api

class WaterCounter(models.Model):
    _name = 'condominium.water_counter'

    # name = fields.Char(string='Propietario', required=True)
    name = fields.Many2one('res.partner',
        ondelete='cascade', string="Propietario", required=True)
    period = fields.Many2one('condominium.period',
        ondelete='cascade', string="Período", required=True)
    old = fields.Float(string='Contador anterior', required=True)
    current = fields.Float(string='Contador actual', required=True)
    date = fields.Date(string="Fecha", required=True)

    # company = fields.Many2one('res.company',
    #     ondelete='cascade', string="Empresa", required=True)
    
    company = fields.Many2one('res.company', 'Company', readonly=True)

    def send_mail_template(self):
        print 'Hey!!!'
        template = self.env.ref('condominium.water_counter_email_template')

        self.env['mail.template'].browse(template.id).send_mail(self.id)

    def print_template(self):
        print "print template!"
        # self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
        return self.env['report'].get_action(self, 'condominium.water_counter_unique_report_pdf')