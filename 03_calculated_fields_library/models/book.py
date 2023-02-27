# -*- coding: utf-8 -*-
from odoo import api, fields, models


class Book(models.Model):
    _inherit = 'ex.book'

    number_of_sheets = fields.Integer(string='Number of sheets', required=True)
    # calculated field____
    extensive_book = fields.Boolean(string="Extensive Books",  compute='_compute_ext_book')

    #calculated field example__
    @api.depends('number_of_sheets')
    def _compute_ext_book(self):
        for record in self:
            record.extensive_book = record.number_of_sheets >= 100



