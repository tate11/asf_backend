# -*- coding: utf-8 -*-
# from odoo.exceptions import UserError, ValidationError
from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.users',
        ondelete='set null', string="Responsible", index=True)

    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")

    # instructor_id = fields.Many2one('res.partner', string="Instructor")
    instructor_id = fields.Many2one('res.partner', string="Instructor",
        domain=['|', ('instructor', '=', True),
                     ('category_id.name', 'ilike', "Teacher")])
    course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

class Partner(models.Model):
    # _name = 'openacademy.partner'
    _inherit = 'res.partner'

    name = fields.Char(required=True)
    is_owner = fields.Boolean(string='Is owner')
    
    apartment_id = fields.Many2many('openacademy.apartment', string="Apartments")
    percent = fields.Float(required=True)

class Apartment(models.Model):
    _name = 'openacademy.apartment'

    name = fields.Char(string='Número', required=True);
    area = fields.Char(string='Área (m2)', required=True);
    percent = fields.Char(string='Porcentaje de participación', required=True);

    tower_id = fields.Many2one('openacademy.tower',
        ondelete='cascade', string="Torre", required=True)
    
    owner_id = fields.Many2one('openacademy.owner',
        ondelete='cascade', string="Propietario", required=True)

class Towers(models.Model):
    _name = 'openacademy.tower'

    name = fields.Char(string='Torre', required=True)

    # @api.onchange('template_id')
    @api.multi
    def create_order(self):
        res = {}
        # self.env['res.partner'].create({'name':'Testing Partner'})
        # return {'warning': {
        #             'title': _('Email addresses not found'),
        #             'message': 'warning_msg',
        #             }
        