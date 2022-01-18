# -*- coding: utf-8 -*-

from odoo import models, fields, api


class device(models.Model):
    _name = 'moqbus.device'
    _description = 'moqbus网关设备'

    name = fields.Char('设备名称', required=True)
    device_id = fields.Char(string='设备ID')
    device_sn = fields.Char(string='设备编号', required=True)
    online = fields.Boolean(string='是否在线')
    ol_update_time = fields.Datetime(string='状态更新时间')
    description = fields.Text(string='备注')
