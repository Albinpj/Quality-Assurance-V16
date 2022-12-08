from odoo import api, fields, models


class QualityMeasure(models.Model):
    _name = "quality.measure"
    _rec_name = "test"
    _description = "Quality Measure"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    test = fields.Text(string='Test')
    product_id = fields.Many2one('product.product', string='Product')
    test_type = fields.Selection(selection=[('qualitative', 'Qualitative'), ('quantitative', 'Quantitative')],
                                 string="Test Type")
    boolean = fields.Boolean(string='Boolean')
    maximum_quantity = fields.Integer(string='maximum')
    minimum_quantity = fields.Integer(string='Minimum')
    trigger_on_ids = fields.Many2many('stock.picking.type', string='Trigger On')

    @api.onchange('test_type')
    def onchange_type(self):
        if self.test_type == "quantitative":
            self.boolean = True
        else:
            self.boolean = False
