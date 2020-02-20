# -*- coding: utf-8 -*-
# from odoo import http


# class Hey!(http.Controller):
#     @http.route('/hey!/hey!/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hey!/hey!/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hey!.listing', {
#             'root': '/hey!/hey!',
#             'objects': http.request.env['hey!.hey!'].search([]),
#         })

#     @http.route('/hey!/hey!/objects/<model("hey!.hey!"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hey!.object', {
#             'object': obj
#         })
