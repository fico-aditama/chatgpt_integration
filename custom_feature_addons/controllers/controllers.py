# -*- coding: utf-8 -*-
# from odoo import http


# class CustomFeatureAddons(http.Controller):
#     @http.route('/custom_feature_addons/custom_feature_addons', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_feature_addons/custom_feature_addons/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_feature_addons.listing', {
#             'root': '/custom_feature_addons/custom_feature_addons',
#             'objects': http.request.env['custom_feature_addons.custom_feature_addons'].search([]),
#         })

#     @http.route('/custom_feature_addons/custom_feature_addons/objects/<model("custom_feature_addons.custom_feature_addons"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_feature_addons.object', {
#             'object': obj
#         })
