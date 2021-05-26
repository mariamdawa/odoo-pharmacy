from odoo import models, fields, api


class Medicine(models.Model):
    _name = 'pharmacy.medicine'
    _description = 'pharmacy.medicine'

    name=fields.Char()
    description=fields.Char()
    price=fields.Float()
    manifacturer=fields.Char()
    order_lines=fields.One2many('pharmacy.orderlines','medicine')