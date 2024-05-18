# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class PurchaseRequest(models.Model):
    _name = "purchase.request"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("custom.purchase.request")
        return super(PurchaseRequest, self).create(vals)

    def action_create_po(self):
        # Create the purchase order lines
        purchase_order_lines = [(0, 0, {
            'product_id': line.product_id.id,
            'name': line.description,
            'product_qty': line.product_qty,
            'product_uom': line.product_uom.id,
        }) for line in self.purchase_order_line_ids]

        purchase_request_record = self.env['purchase.request'].browse(self.id)
        purchase_request_abs = self.env['purchase.request.abs'].create({
            # 'supplier': self.request_by,
            'name': self.name,
            'purchase_request_id': purchase_request_record.id,
            'purchase_order_line_ids': purchase_order_lines,
        })

        # Open a popup view for the created purchase order
        return {
            'name': 'Create Purchase Order',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'purchase.request.abs',
            'target': 'new',
            'res_id': purchase_request_abs.id,
            'context': self.env.context,
        }

    def action_close_po(self):
        self.write({'state':'closed'})

    @api.depends('purchase_order_ids')
    def _compute_purchase_order_summary(self):
        for request in self:
            request.count_total_purchase_order = len(request.purchase_order_ids)

    def action_get_purchase_order_view(self):
        purchase_orders = self.mapped('purchase_order_ids')
        return {
            'name': 'Purchase Orders',
            'view_mode': 'tree,form',
            'res_model': 'purchase.order',
            'type': 'ir.actions.act_window',
            'target': 'new',
            'domain': [('id', 'in', purchase_orders.ids)],
        }
    @api.model
    def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
        result = super(PurchaseRequest, self).fields_view_get(
            view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)

        if view_type == 'form':
            button = {
                'name': 'action_get_purchase_order_view',
                'string': 'View Purchase Orders',
                'type': 'object',
                'class': 'btn-primary',
            }
            result['buttons'] = result.get('buttons', []) + [button]

        return result

    @api.depends('request_by')
    def _compute_employee_id(self):
        self.employee_id = False
        self.department_id = False
        for record in self:
            if record.request_by:
                # record.employee_id = record.request_by.employee_ids[0].id
                record.department_id = record.request_by.employee_ids[0].department_id.id

    name = fields.Char(string='Purchase Request', readonly=True)
    purchase_order_ids = fields.One2many('purchase.order','purchase_request_id', string='Purchase Order')
    request_by = fields.Many2one('res.users', string='Request By', default=lambda self: self.env.user)
    count_total_purchase_order = fields.Integer(string='Purchase Order Summary', compute='_compute_purchase_order_summary')

    # employee_id = fields.Many2one('hr.employee', string='Employee', compute='_compute_employee_id', store=True)
    department_id = fields.Many2one('hr.department', string='Department')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting Approval'),
        ('approved', 'Approved'),
        ('closed', 'Closed'),
    ], string='Order Category')

    date = fields.Date(string='Date', default=fields.Date.today)
    order_category = fields.Selection([
        ('bahan_baku_produksi', 'Bahan Baku Produksi'),
        ('bahan_pendukung_produksi', 'Bahan Pendukung Produksi'),
        ('asset', 'Asset'),
        ('barang_khusus', 'Barang Khusus'),
        ('operational', 'Operational'),
        ('other', 'Lain-lain'),
    ], string='Order Category')
    created_on = fields.Date(default=fields.Date.today)
    company_id = fields.Many2one('res.partner', string='Company')
    is_asset = fields.Boolean('Asset')
    purchase_order_line_ids = fields.One2many('purchase.request.line', 'purchase_request_id', string='Order Lines')

class PurchaseRequestLine(models.Model):
    _name = "purchase.request.line"

    @api.onchange('product_id','purchase_request_id','purchase_request_abs_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.description = self.product_id.name
        if self.purchase_request_abs_id:
            self.name = self.purchase_request_abs_id
        if self.purchase_request_id:
            self.name = self.purchase_request_id
        if self.product_uom:
            self.product_uom = self.product_id.uom_id.id

    name = fields.Char(string='Name')
    purchase_request_id = fields.Many2one('purchase.request', string='Purchase Request')
    purchase_request_abs_id = fields.Many2one('purchase.request.abs', string='Purchase Request')
    product_id = fields.Many2one('product.product', string='Product')
    price_total = fields.Float(string='Price Total')
    description = fields.Char(string='Description')
    product_qty = fields.Integer(string='Qty')
    product_uom = fields.Many2one('uom.uom', string='UOM')
    stock = fields.Float(string='Stock on Hand', related='product_id.qty_available')

class PurchaseRequestAbs(models.Model):
    _name = "purchase.request.abs"

    def action_create_po(self):
            # Create the purchase order lines
            purchase_order_lines = [(0, 0, {
                'product_id': line.product_id.id,
                'name': line.name,
                'product_qty': line.product_qty,
                'product_uom': line.product_uom.id,
            }) for line in self.purchase_order_line_ids]

            # Create the purchase order
            purchase_order = self.env['purchase.order'].create({
                'partner_id': self.supplier.id,  # Assuming self.supplier is the supplier
                'origin': self.name,
                'purchase_request_id': self.purchase_request_id.id,
                'order_line': purchase_order_lines,
            })

            # Open a popup view for the created purchase order
            return {
                'name': 'Purchase Order',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'purchase.order',
                'target': 'current',
                'res_id': purchase_order.id,
                'context': self.env.context,
            }

    def action_cancel_purchase_request(self):
        return {'type': 'ir.actions.act_window_close'}

    name = fields.Char(string='Request')
    supplier = fields.Many2one('res.partner', string='Supplier')
    purchase_request_id = fields.Many2one('purchase.request', string='Purchase Request')
    purchase_order_line_ids = fields.One2many('purchase.request.line','purchase_request_abs_id', string='Purchase Order Lines')