# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Courses(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    user_id = fields.Many2one('res.users', string="Responsible")


class Sessions(models.Model):
    _name = 'openacademy.session'

    course_id = fields.Many2one('openacademy.course', string="Course")
    user_id = fields.Many2one('res.users', string="Instructor")
    start_date = fields.Date()
    seats = fields.Integer('Room Capacity')
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    number_of_attendees = fields.Integer(compute='_nbAttendees')
    
    @api.depends('attendee_ids')
    
    def _nbAttendees(self):
        for record in self:
            record.number_of_attendees = len(record.attendee_ids)
            
    #@api.onchange('number_of_attendees') # if these fields are changed, call method
    #def check_change(self):
    #    if self.number_of_attendees > 3:
    #        raise ValidationError("Too many attendees for this session.")
            
    @api.constrains('attendee_ids', 'seats')
    def _check_number(self):
        print('hello world')
        if len(self.attendee_ids) > self.seats:
            raise ValidationError("Too many attendees for this session.")