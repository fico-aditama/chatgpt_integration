# -*- coding: utf-8 -*-
# from odoo import http


# class ChatgptIntegration(http.Controller):
#     @http.route('/chatgpt_integration/chatgpt_integration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chatgpt_integration/chatgpt_integration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chatgpt_integration.listing', {
#             'root': '/chatgpt_integration/chatgpt_integration',
#             'objects': http.request.env['chatgpt_integration.chatgpt_integration'].search([]),
#         })

#     @http.route('/chatgpt_integration/chatgpt_integration/objects/<model("chatgpt_integration.chatgpt_integration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chatgpt_integration.object', {
#             'object': obj
#         })
