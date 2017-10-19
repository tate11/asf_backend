# -*- coding: utf-8 -*-

from odoo import fields, models

class ReportMantainanceFeeWizard(models.TransientModel):

    _name = "condominium.report_mantainance_fee_wizard"
    _description = "Reporte de mantenimiento"

    report_name = fields.Char('Nombre del reporte', required=True)
    # mantainance_fee_ids = fields.Char('Cuotas de mantenimiento', required=True)
    
    # mantainance_fee_ids = fields.many2many(
    #                         'sale.order',
    #                         'unefa_estudiante_reporte_wizard_rel',
    #                         'estudiante_id',
    #                         'reporte_id',
    #                         'Estudiantes')

    # mantainance_fee_ids = fields.Many2many('ir.model.fields', string='Fields to use', domain="[('model_id', '=', model_names )]")
    mantainance_fee_ids = fields.Many2many(
                            'sale.order', 
                            string='Cuotas de mantenimiento pendientes de pago', 
                            domain="[('is_maintenance_fee', '=', 'True'),('state', '!=', 'done')]")

    def report_mantainance_fee_pdf(self,cr,uid,ids,context=None):
        report_data = self.browse(cr,uid,ids,context=context)
        data = {'title':report_data.report_name,'ids':ids}

        return self.pool['report'].get_action(cr,uid,[],'condominium.mantainance_fee_wizard_qweb',data=data,context=context)