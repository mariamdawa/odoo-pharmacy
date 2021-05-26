from odoo import models,api,fields

class Orders(models.Model):
    _name="pharmacy.orders"
    _description="pharmacy.orders"

    customer=fields.Many2one('res.partner')
    date=fields.Date()

    orderlines=fields.One2many('pharmacy.orderlines','orders')
    total_price=fields.Float(compute='calc_total',store=True)

    @api.depends('orderlines.sub_total')
    @api.onchange('orderlines')
    def calc_total(self):
        for order in self:
            for record in order.orderlines:
                order.total_price += record.sub_total
