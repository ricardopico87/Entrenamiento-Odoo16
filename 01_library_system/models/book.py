# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Book(models.Model):
    _name = 'ex.book'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    loan_number = fields.Integer(string='Loan Number', required=True)
    section = fields.Integer(string='Section')
    code = fields.Char(string='code', default="New", readonly=1)
    edition_new = fields.Boolean(string='Edition New')
    gender = fields.Selection([
        ('fantastic', 'Fantastic'),
        ('adventure', 'Adventure'),
        ('infantile', 'Infantile'),
        ('historical', 'Historical'),
        ('other', 'Other')], string='type', default="adventure")


    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code('ex.book') or "Nuevo"
            book = super(Book, self).create(vals)
            return book