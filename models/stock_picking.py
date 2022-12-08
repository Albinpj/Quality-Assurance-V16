from odoo import models, fields
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'


    def quality_checks(self):
        list1 = []
        product = []
        measure1 = []
        for line1 in self.move_ids_without_package:
            list1.append(line1.product_id.id)
            print(list1)
        measure = self.env['quality.measure'].search(
            [('trigger_on_ids', 'in', self.picking_type_id.id)])
        product.append(measure.product_id.id)
        print(product)
        for i in list1:
            for j in product:
                if i == j:
                    if j not in measure1:
                        measure1.append(j)
        print(measure1)
        if measure1:
            for j in measure1:
                self.env['quality.alert'].create([
                    {
                        'product_id': j,
                        'date': self.scheduled_date,
                        'source_operation': self.id,
                    }, ])

            return {
                'type': 'ir.actions.act_window',
                'name': 'Quality Alert',
                'view_mode': 'tree,form',
                'res_model': 'quality.alert',
                'context': "{'create': True}",
            }
        else:
            print("else")
            raise ValidationError('This Transfer Have No Matching Quality Measure')

    def button_validate(self):
        res = super(StockPicking, self).button_validate()
        list1 = []
        test = self.env['quality.test'].search([('status', '=', 'fail')])
        print(test)
        list1.append(test.stock_picking)
        print(list1)
        for i in list1:
            for j in i:
                if self.id == j.id:
                    raise ValidationError('This Transfer Failed In The Quality Test')
        return res


