# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Book(models.Model):
    _inherit = 'ex.book'

    quantity_in_stock = fields.Integer(string='Quantity in stock', required=True)
    loan_date = fields.Date(string="Loan Date")



