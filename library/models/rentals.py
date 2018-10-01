# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')
    rental_date = fields.Date(string='Rental date')
    return_date = fields.Date(string='Return date')
    email = fields.Char(string='Customer email', related='customer_id.email')
    
#    @api.onchange('customer_id','book_id')
#    def _display_info(self):
#        name = fields.Char(related='library.partner.name')
