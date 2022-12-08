from odoo import api, fields, models


class QualityTest(models.Model):
    _name = "quality.test"
    _rec_name = "measure_id"
    _description = "Quality Test"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    test_type = fields.Selection(selection=[('qualitative', 'Qualitative'), ('quantitative', 'Quantitative')],
                                 string="Test type")
    boolean = fields.Boolean(string='Boolean')
    maximum_quantity = fields.Integer(string='maximum')
    minimum_quantity = fields.Integer(string='Minimum')
    result = fields.Selection(selection=[('satisfied', 'Satisfied'), ('unsatisfied', 'Unsatisfied')],
                              string="Result")
    status = fields.Selection(selection=[('pass', 'Pass'), ('fail', 'Fail')],
                              string="Status")
    measure_id = fields.Many2one('quality.measure', string='Quality Measure')
    quality_alert_id = fields.Many2one('quality.alert', string='Quality Alert')
    product_id = fields.Many2one('product.product', string='Product')
    stock_picking = fields.Many2one('stock.picking',string="Stock Picking")

    @api.onchange('result')
    def onchange_result(self):
        if self.result == "satisfied":
            self.status = 'pass'
        else:
            self.status = 'fail'

    @api.onchange('test_type')
    def onchange_type(self):
        if self.test_type == "quantitative":
            self.boolean = True
        else:
            self.boolean = False


