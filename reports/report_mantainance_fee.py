# -*- encoding: utf-8 -*-
import odoo
from odoo.report import report_sxw
from odoo.osv import osv

class mantainance_fee_report(report_sxw.rml_parse):
    def __init__(self,cr,uid,name,context):
        super(mantainance_fee_report,self).__init__(cr,uid,name,context)
        self.localcontext.update({
            # 'get_data_mantainance_fee':self.get_data_mantainance_fee
            'get_data_mantainance_fee':self.render_html
            })
    
    def get_data_mantainance_fee(self,id_wizard):
        wizard_obj=self.pool.get('condominium.report_mantainance_fee_wizard')
        wizard_data=wizard_obj.browse(self.cr,self.uid,id_wizard)
        return wizard_data.mantainance_fee_ids

    # @api.model
    def render_html(self, docids, data=None):
        report_obj = self.env['report']
        report = report_obj._get_report_from_name('condominium.mantainance_fee_report_pdf')
        docargs = {
            'doc_ids': docids,
            'doc_model': report.model,
            'docs': self,
        }
        return report_obj.render('condominium.mantainance_fee_report_pdf', docargs)
 

class report_mantainance_fee_wizard(osv.AbstractModel):
    _name="report.condominium.mantainance_fee_wizard_qweb"
    _inherit="report.abstract_report"
    _template="condominium.mantainance_fee_wizard_qweb"
    _wrapped_report_class=mantainance_fee_report
    

class mantainance_fee_report_pdf(osv.AbstractModel):
    _name = "report.condominium.mantainance_fee_report_pdf"
    _inherit = "report.abstract_report"
    _template = "condominium.mantainance_fee_report_pdf"
    _wrapped_report_class = mantainance_fee_report