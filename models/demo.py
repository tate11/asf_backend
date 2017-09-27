from openerp import fields,models
class sale_order(models.Model):
     _inherit='sale.order'
     field_One2many=field.One2many('sale.order.line','order_id','Order')
sale_order()
class sale_order_line(models.model):
     _inherit='sale.order.line'
     order_id=fields.Many2one('sale.order','Order')
sale_order_line()