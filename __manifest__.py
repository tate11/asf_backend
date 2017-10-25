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
    'depends': ['base','sale','web','web_tour'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/functions/condominium_functions.xml',
        'views/product_template_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/sale_order_line_views.xml',
        'views/condominium_views.xml',
        'views/res_company_views.xml',
        'views/tower_views.xml',
        'views/floor_views.xml',
        'views/so_views.xml',
        'views/water_counter_views.xml',
        'views/period_views.xml',
        'views/water_default_item_views.xml',
        'views/tour/condominium_tour.xml',
        'views/dashboards/widget_view.xml',
        # 'actions/sale_order_views.xml',
        'reports/report_mantainance_fee_views.xml',
        'reports/report_water_counter_views.xml',
        'reports/payment_order_views.xml',
        'templates/report_mantainance_fee_views.xml',
        'templates/report_water_counter_list_views.xml',
        'templates/report_water_counter_unique_views.xml',
        'templates/email_mantainance_fee_views.xml',
        'templates/email_water_counter_views.xml',
        # 'dashboards/dashboard_kanban_view.xml',
        # 'dashboards/water_counter_dashboard_view.xml',
        'datas/tower_data.xml',
        'datas/floor_data.xml',
        'datas/period_data.xml',
        'datas/apartment_data.xml',
        'datas/depot_data.xml',
        'datas/parking_data.xml',
        'datas/facility_data.xml',
        'datas/dashboard.xml',
        # 'wizards/report_mantainance_fee_wizard.xml'
    ],
}