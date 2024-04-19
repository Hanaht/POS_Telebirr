from odoo import models, fields

class PaymentStatus(models.Model):
    _name = 'telebirr_payment.status'
    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
    payer_id = fields.Many2one('res.partner', string='Payer')
    pos_config = fields.Many2one('pos.config', string='POS Configuration')
    trace_number = fields.Char(string='Trace Number')
