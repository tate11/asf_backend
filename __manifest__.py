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
        # 'views/templates.xml',
        'views/openacademy.xml',
        # 'views/owners.xml',
        # 'views/mail_template.xml',
        'views/contact_view.xml',
        'views/quotation_view.xml',
        # 'views/condominium.xml',

    ],
}