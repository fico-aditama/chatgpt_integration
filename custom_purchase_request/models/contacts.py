# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Contact(models.Model):
    _inherit = "res.partner"

    contact_type = fields.Selection([
        ('customer', 'Customer'),
        ('supplier', 'Supplier')
    ], string='Contact Type')

    customer_code = fields.Char(string='Customer Code')