# -*- coding: utf-8 -*-
# from odoo import http


# class CustomModuleSanqua(http.Controller):
#     @http.route('/custom_module_sanqua/custom_module_sanqua/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_module_sanqua/custom_module_sanqua/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_module_sanqua.listing', {
#             'root': '/custom_module_sanqua/custom_module_sanqua',
#             'objects': http.request.env['custom_module_sanqua.custom_module_sanqua'].search([]),
#         })

#     @http.route('/custom_module_sanqua/custom_module_sanqua/objects/<model("custom_module_sanqua.custom_module_sanqua"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_module_sanqua.object', {
#             'object': obj
#         })
