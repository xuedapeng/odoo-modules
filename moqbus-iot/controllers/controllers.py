# -*- coding: utf-8 -*-
# from odoo import http


# class Moqbus-iot(http.Controller):
#     @http.route('/moqbus-iot/moqbus-iot', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/moqbus-iot/moqbus-iot/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('moqbus-iot.listing', {
#             'root': '/moqbus-iot/moqbus-iot',
#             'objects': http.request.env['moqbus-iot.moqbus-iot'].search([]),
#         })

#     @http.route('/moqbus-iot/moqbus-iot/objects/<model("moqbus-iot.moqbus-iot"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('moqbus-iot.object', {
#             'object': obj
#         })
