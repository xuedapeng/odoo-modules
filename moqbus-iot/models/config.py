# -*- coding: utf-8 -*-

from odoo import models, fields, api


class config(models.Model):
    _name = 'moqbus.config'
    _description = 'moqbus组态'

    name = fields.Char('组态名称', required=True)
    type = fields.Selection([('qxz', '气象站'), ('ddf', '电动阀'), ('dpjlj', '大棚卷帘机')], string='设备类型', required=True)
    project_id = fields.Integer(string='组态ID', required=True)
    url = fields.Char(string='API地址')
    secret_id = fields.Char(string='授权Id', required=True)
    secret_key = fields.Char(string='授权Key', required=True)
    gateway = fields.Many2many('moqbus.device', string='网关', required=True)
    description = fields.Text()
