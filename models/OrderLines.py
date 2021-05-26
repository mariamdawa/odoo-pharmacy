from odoo import models, fields, api
from . import Medicine


class OrderLines(models.Model):
    _name="pharmacy.orderlines"
    _description="pharmacy.orderlines"

    medicine=fields.Many2one('pharmacy.medicine')
    unit_price=fields.Float(compute="get_price",store=True)
    quantity=fields.Integer()
    sub_total=fields.Float(compute='calc_sub_total',store=True)
    orders=fields.Many2one('pharmacy.orders')

    @api.depends('medicine.price')
    @api.onchange('medicine')
    def get_price(self):
        for record in self:
            record.unit_price=record.medicine.price

    @api.depends('quantity','medicine.price')
    @api.onchange('quantity','medicine')
    def calc_sub_total(self):
        for record in self:
            record.sub_total=record.unit_price * record.quantity