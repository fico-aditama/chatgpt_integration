# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("custom.purchase.order")
        return super(PurchaseOrder, self).create(vals)

    purchase_request_id = fields.Many2one('purchase.request', string='Purchase Order')
