from odoo import api, fields, models, tools, _
import datetime

class List(models.Model):
    _inherit = 'purchase.order.line'

    x_project = fields.Char(string=u'项目号',compute='_get_project',store=True)
    x_remark = fields.Char(string=u'备注',compute='_get_project',store=True)
    x_name = fields.Char(string=u'需求者',compute='_get_project',store=True)
    x_date = fields.Char(string=u'需求时间',compute='_get_project',store=True)

    @api.constrains('order_id')
    def _get_project(self):
        if self.order_id:
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
                            ss.append( datetime.datetime.strftime(i.add_warehouse_orderpoint, "%Y-%m-%d"))
                obj.x_project=dd
                obj.x_remark=ee
                obj.x_name=ff
                obj.x_date=ss
