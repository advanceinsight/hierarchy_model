# -*- coding: utf-8 -*-
from odoo import http


# class AcModule(http.Controller):
#     @http.route('/ac_module/ac_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ac_module/ac_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ac_module.listing', {
#             'root': '/ac_module/ac_module',
#             'objects': http.request.env['ac_module.ac_module'].search([]),
#         })

#     @http.route('/ac_module/ac_module/objects/<model("ac_module.ac_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ac_module.object', {
#             'object': obj
#         })
