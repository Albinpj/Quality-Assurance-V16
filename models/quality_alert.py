from odoo import api, fields, models


class QualityAlert(models.Model):
    _name = "quality.alert"
    _rec_name = "sequence"
    _description = "Quality Alert"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    product_id = fields.Many2one('product.product', string='Product')
    created_by_id = fields.Many2one('res.users', string='Created By')
    date = fields.Datetime(string='Date')
    source_operation = fields.Many2one('stock.picking', string='Source Operation')
    sequence = fields.Char(string="Sequence Number", readonly=True, required=True, copy=False, default='New')
    test_ids = fields.One2many('quality.test', 'quality_alert_id', string='Test')

    @api.model
    def create(self, vals):
        if vals.get('sequence', 'New') == 'New':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('quality.alert') or 'New'
        result = super(QualityAlert, self).create(vals)
        return result

    def action_create_test(self):
        quality_test_id = self.env['quality.test'].create([
            {'quality_alert_id': self.id,
             'product_id': self.product_id.id,
             'stock_picking': self.source_operation.id,
             }, ])
        return {
            'type': 'ir.actions.act_window',
            'name': 'Quality Test',
            'view_mode': 'form',
            'res_model': 'quality.test',
            'res_id': quality_test_id.id,
            'context': "{'create': True}"
        }


