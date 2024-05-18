# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    @api.model
    def create(self, vals):
        # code is a reference for 'Operation Type' divide by three is "Internal", "Delivery" and "Receipt"
        if self.picking_type_id.code == 'outgoing':
            vals["name"] = self.env["ir.sequence"].next_by_code("custom.stock.picking.do")
        elif self.picking_type_id.code == 'incoming':
            vals["name"] = self.env["ir.sequence"].next_by_code("custom.stock.picking.gr")
    
        return super(StockPicking, self).create(vals)
