# -*- coding: utf-8 -*-
# from odoo import http


# class CustomDashboard(http.Controller):
#     @http.route('/custom_dashboard/custom_dashboard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_dashboard/custom_dashboard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_dashboard.listing', {
#             'root': '/custom_dashboard/custom_dashboard',
#             'objects': http.request.env['custom_dashboard.custom_dashboard'].search([]),
#         })

#     @http.route('/custom_dashboard/custom_dashboard/objects/<model("custom_dashboard.custom_dashboard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_dashboard.object', {
#             'object': obj
#         })
