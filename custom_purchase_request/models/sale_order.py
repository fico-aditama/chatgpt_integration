import json
from odoo import models, fields, api, _
from datetime import datetime
from odoo.tools import date_utils, json

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("custom.sale.order")
        return super(SaleOrder, self).create(vals)

class SaleOrderReport(models.TransientModel):
    _name = 'sale.order.report'
    _description = 'Sale Net Report'

    sale_order_ids = fields.Many2many('sale.order')
    date_from = fields.Datetime(string='Date From')
    date_to = fields.Datetime(string='Date To')

    def get_analysis_report(self):
        domain = []
        if self.sale_order_ids:
            domain.append(('id', 'in', self.sale_order_ids.ids))
        if self.date_from:
            domain.append(('date_order', '>=', self.date_from))
        if self.date_to:
            domain.append(('date_order', '<=', self.date_to))

        sale_orders = self.env['sale.order'].search(domain)

        sale_order_list = []
        for order in sale_orders:
            
            order_lines = []
            for line in order.order_line:
                delivered_qty = 0
                return_qty = 0
                # for picking in order.picking_ids:
                #     if picking.picking_type_code == 'outgoing' and picking.state == 'done':
                #         for move in picking.move_lines.filtered(lambda m: m.product_id == line.product_id):
                #             if move.location_dest_id.usage == 'customer':
                #                 delivered_qty += move.quantity_done
                #             elif move.location_dest_id.usage == 'supplier':
                #                 return_qty += move.quantity_done
                
                order_lines.append({
                    'product_id': line.product_id.display_name,
                    'demand': line.product_uom_qty,
                    'done': line.qty_delivered,
                    'return': return_qty ,  
                    'net': line.qty_delivered - return_qty,  
                })
            record = {
                'do_number': order.picking_ids.name if order.picking_ids else None,
                'so_number_id': order.name,
                'customer_code': order.partner_id.customer_code,
                'customer_name': order.partner_id.name,
                'customer_address': order.partner_id.street,
                'delivery_date': order.commitment_date,
                'company_id': order.company_id.name,
                'order_lines': order_lines,
                'invoice_number': order.invoice_ids[0].number if order.invoice_ids else '',
                'total_invoice': order.amount_total if order.invoice_ids else 0.0,
            }
            sale_order_list.append(record)
        datas = {
            'form_data': self.read()[0],
            'sale_order': sale_order_list,
            'start_date': self.date_from,
            'end_date': self.date_to,
        }

        return self.env.ref('custom_module_sanqua.report_sale_order_net').report_action(self, data=datas)
