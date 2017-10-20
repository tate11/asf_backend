# -*- coding: utf-8 -*-
{
    'name': "Condominium",

    'summary': """Condominium APP""",

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,

    'author': "Aranda Software Company",
    'website': "http://www.arandasf.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','contacts','sale','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template.xml',
        'views/res_partner.xml',
        'views/sale_order.xml',
        'views/sale_order_line.xml',
        'views/condominium.xml',
        'views/res_company.xml',
        'views/tower.xml',
        'views/floor.xml',
        'views/so.xml',
        'views/water_counter.xml',
        'views/period.xml',
        'views/water_default_item.xml',
        'views/settings.xml',
        'actions/sale_order.xml',
        'reports/report_mantainance_fee.xml',
        'reports/payment_order.xml',
        'templates/report_mantainance_fee.xml',
        'templates/email_mantainance_fee.xml',
        # 'wizards/report_mantainance_fee_wizard.xml'
    ],
}