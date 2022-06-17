# -*- coding: utf-8 -*-
{
    'name': 'add_warehouse_orderpoint',
    'category': 'add_warehouse_orderpoint',
    'description': """
            add_warehouse_orderpoint
            """,
    'author': 'CodeFire Technologies',
    'website': 'https://www.codefire.org/',
    'version': '14.0.1.0',
    'license': 'AGPL-3',
    'images': ['static/description/odoo-free.jpg'],
    'depends': [
        'purchase','stock'
    ],
    "data": [
        "views/sale_stock.xml",
        "views/sale_list.xml",
        "views/stock_pickings.xml",
        "views/view_move_form.xml",
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
