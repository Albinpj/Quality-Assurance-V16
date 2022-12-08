{
    'name': 'Quality Assurance',
    'version': '16.0.1.0',
    'sequence': -101,
    'category': 'Quality Assurance',
    'summary': 'Quality Assurance For Inventery Moves',
    'application': True,
    'depends': [
        'base',
        'product',
        'stock'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/quality_menus.xml',
        'views/quality_measure.xml',
        'views/quality_alert.xml',
        'views/quality_test.xml',
        'views/quality_test.xml',
        'views/stock_picking.xml',
        'data/sequence.xml',

    ],
}
