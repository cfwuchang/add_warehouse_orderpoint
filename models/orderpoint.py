from odoo import api, fields, models, tools, _
from odoo import SUPERUSER_ID, _, api, fields, models, registry
from odoo.tools import add, float_compare, frozendict, split_every, format_date
from odoo.addons.stock.models.stock_rule import ProcurementException

import logging
from psycopg2 import OperationalError
from datetime import datetime, time

_logger = logging.getLogger(__name__)
class Orderpoint(models.Model):
    _inherit = 'stock.warehouse.orderpoint'

    x_project = fields.Char(string=u'项目号')
    x_remark = fields.Char(string=u'备注')
    x_name = fields.Char(string=u'需求者')
    x_date = fields.Char(string=u'需求时间')


    def create_batch(self):
        att_model = self.env['stock.move']
        for obj in self:
            query = [("reference","ilike","WH/MO"),("state","!=","done"),("state","!=","cancel"),("state","!=","draft")]
            dd=[]
            ee=[]
            ff=[]
            ss=[]
            for i in att_model.search(query):
                if obj.product_id ==i.product_id:
                    if i.product_uom_qty==i.forecast_availability:
                       continue
                    else: 
                        dd.append(i.raw_material_production_id.product_id.name)
                        ee.append(i.x_remark)
                        ff.append(i.create_uid.name)
                        ss.append( datetime.strftime(i.date_move_list, "%Y-%m-%d"))
            obj.x_project=dd
            obj.x_remark=ee
            obj.x_name=ff
            obj.x_date=ss
    # def action_replenish(self):
    #     self._procure_orderpoint_confirm(company_id=self.env.company)

    #     notification = False
    #     if len(self) == 1:
    #         notification = self._get_replenishment_order_notification()
    #     # Forced to call compute quantity because we don't have a link.
    #     self._compute_qty()
    #     self.filtered(lambda o: o.create_uid.id == SUPERUSER_ID and o.qty_to_order <= 0.0 and o.trigger == 'manual').unlink()
    #     return notification
        
    
   


  
