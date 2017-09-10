# -*- coding: utf-8 -*-
from odoo import http

# class LoginUserDetailExtended(http.Controller):
#     @http.route('/login_user_detail_extended/login_user_detail_extended/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/login_user_detail_extended/login_user_detail_extended/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('login_user_detail_extended.listing', {
#             'root': '/login_user_detail_extended/login_user_detail_extended',
#             'objects': http.request.env['login_user_detail_extended.login_user_detail_extended'].search([]),
#         })

#     @http.route('/login_user_detail_extended/login_user_detail_extended/objects/<model("login_user_detail_extended.login_user_detail_extended"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('login_user_detail_extended.object', {
#             'object': obj
#         })