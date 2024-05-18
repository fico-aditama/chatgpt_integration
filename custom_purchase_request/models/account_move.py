# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.model
    def create(self, vals):
        vals["name"] = self.env["ir.sequence"].next_by_code("custom.account.move")
        return super(AccountMove, self).create(vals)
