from odoo import api,fields,models,_
import datetime
class StockPickings(models.Model):
    _inherit = "stock.move"
    
    x_project = fields.Char(string=u'项目号',related ='purchase_line_id.x_project',store=True)