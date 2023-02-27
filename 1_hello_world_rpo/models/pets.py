from odoo import fields, models, api
class PetsRPO(models.Model):
    _name = 'pets.rpo'
# atributos de la clase que estaran en la vista form.
    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age', required=True)
    color = fields.Char(string='color', required=True)
    type = fields.Selection([
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        ('fish', 'Fish'),
        ('reptil', 'Reptil'),
        ('roedor', 'Roedor'),
        ('other', 'Other')], string='type', default="dog")


