# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Book(models.Model):
    _name = 'ex.book'

    title = fields.Char(string='title', required=True)
    author = fields.Char(string='author', required=True)
    loan_number = fields.Integer(string='loan_number', required=True)
    section = fields.Integer(string='section')
    edition_new = fields.Boolean(string='edition_new')
    gender = fields.Selection([
        ('fantastic', 'Fantastic'),
        ('adventure', 'Adventure'),
        ('infantile', 'Infantile'),
        ('historical', 'Historical'),
        ('other', 'Other')], string='type', default="adventura")


