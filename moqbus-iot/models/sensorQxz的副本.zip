# -*- coding: utf-8 -*-

import datetime
import json
import os
import sys
from datetime import timedelta

from odoo import models, fields
from .. import logic


def update_sensors_by_config(record, model_qxz):
    projectId = record.config.project_id
    secretId = record.config.secret_id
    secretKey = record.config.secret_key
    url = record.config.url

    resultMap = logic.moqbus_api.Moqbus.uiconfig_data_get(projectId, secretId, secretKey, url)

    if resultMap is None:
        return
    else:
        for sn in resultMap:
            for sno in resultMap[sn]:
                ds = model_qxz.search([('device.device_sn', '=', sn), ('sensor_no', '=', sno)])
                for rs in ds:
                    rs.fd_wd = resultMap[sn][sno]["wd"]
                    rs.fd_sd = resultMap[sn][sno]["sd"]
                    rs.fd_gz = resultMap[sn][sno]["gz"] if "gz" in resultMap[sn][sno] else None
                    rs.fd_co2 = resultMap[sn][sno]["nd"] if "nd" in resultMap[sn][sno] else None
                    update_time = datetime.datetime.strptime(resultMap[sn][sno]["time"], "%Y-%m-%d %H:%M:%S")
                    update_time = update_time - timedelta(hours=8)
                    rs.update_time = fields.Datetime.to_datetime(update_time)


def calc_ago_time(baseTime):
    if baseTime is None:
        return ""

    intv = (datetime.datetime.now() - baseTime).total_seconds()
    if intv < 60:
        return "现在"
    elif intv < 3600:
        return str(int(intv / 60)) + "分钟前"
    elif intv < 3600 * 24:
        return str(int(intv / 3600)) + "小时前"
    elif intv < 3600 * 24 * 30:
        return str(int(intv / (3600 * 24))) + "天前"
    elif intv < 3600 * 24 * 365:
        return str(int(intv / (3600 * 24 * 30))) + "个月前"
    else:
        return str(int(intv / (3600 * 24 * 365))) + "年前"


class sensorQxz(models.Model):
    _name = 'moqbus.sensor.qxz'
    _description = 'moqbus气象站'

    name = fields.Char('传感器名称', required=True)
    device = fields.Many2one('moqbus.device', string='网关', required=True)
    device_ol = fields.Boolean(compute='_get_device_ol', string='是否在线')
    device_sn = fields.Char(compute='_get_device_sn', string='网关编号')
    sensor_no = fields.Integer(string='传感器序号', default=None, required=True)
    config = fields.Many2one('moqbus.config', string='组态', required=True)
    fd_wd = fields.Char(string='温度(℃)', default=None)
    fd_sd = fields.Char(string='湿度(%)', default=None)
    fd_gz = fields.Char(string='光照(LUX)', default=None)
    fd_co2 = fields.Char(string='CO₂浓度(PPM)', default=None)
    update_time = fields.Datetime(string='数据更新时间')
    ago_time = fields.Char(compute='_get_ago_time', string='更新时间')
    cmd_query = fields.Char(string='查询命令', required=True)
    description = fields.Text(string="备注")

    def do_refresh(self):
        for record in self:
            # record.fd_wd = 13
            update_sensors_by_config(record, self.env["moqbus.sensor.qxz"])

    def _get_device_ol(self):
        for record in self:
            record.device_ol = record.device.online

    def _get_device_sn(self):
        for record in self:
            record.device_sn = record.device.device_sn

    def _get_ago_time(self):
        for record in self:
            record.ago_time = logic.moqbus_api.Moqbus.calc_ago_time(record.update_time)
