from odoo import models,api,fields

class Customer(models.Model):
    _name="pharmacy.customer"
    _inherit = 'res.partner'

    name=fields.Char()
    orders=fields.One2many('pharmacy.orders','customer')