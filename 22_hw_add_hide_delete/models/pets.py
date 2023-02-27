from odoo import api, models, fields

class Pets(models.Model):
    #heredando de la clase pets que define el resto de atributos
    _inherit = 'pets.rpo'

    #nuevos atributos agregados
    vaccinated = fields.Boolean(string='Vaccinated')
    adopted_time = fields.Integer(string='Adopted Time')

    @api.onchange('adopted_time')
    def _onchange_account_type(self):
        if self.adopted_time:
            self.age = self.adopted_time

    @api.model
    def create(self, values):
        values['age'] = values["adopted_time"]
        # Add code here
        return super(Pets, self).create(values)