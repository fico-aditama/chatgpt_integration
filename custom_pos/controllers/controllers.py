# -*- coding: utf-8 -*-
# from odoo import http


# class CustomPos(http.Controller):
#     @http.route('/custom_pos/custom_pos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_pos/custom_pos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_pos.listing', {
#             'root': '/custom_pos/custom_pos',
#             'objects': http.request.env['custom_pos.custom_pos'].search([]),
#         })

#     @http.route('/custom_pos/custom_pos/objects/<model("custom_pos.custom_pos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_pos.object', {
#             'object': obj
#         })
