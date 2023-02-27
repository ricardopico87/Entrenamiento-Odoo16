# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Book(models.Model):
    _name = 'ex.book'

    title = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    loan_number = fields.Integer(string='Loan Number', required=True)
    section = fields.Integer(string='Section')
    edition_new = fields.Boolean(string='Edition New')
    gender = fields.Selection([
        ('fantastic', 'Fantastic'),
        ('adventure', 'Adventure'),
        ('infantile', 'Infantile'),
        ('historical', 'Historical'),
        ('other', 'Other')], string='type', default="adventura")


