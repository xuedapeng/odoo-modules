# -*- coding: utf-8 -*-
import datetime

import requests
import json

REQUEST_URL = "http://cloud.moqbus.com/open/api/"
HEADER = {'Content-Type': 'application/json; charset=utf-8'}


class Moqbus:

    @staticmethod
    def uiconfig_data_get(projectId, secretId, secretKey, url=REQUEST_URL):
        if url is None:
            url = REQUEST_URL

        requestDict = {"method": "uiconfig.data.get", "data": {"projectId": str(projectId), "childs": "no"},
                       "auth": [secretId, secretKey]}
        rsp = requests.post(REQUEST_URL, data=json.dumps(requestDict), headers=HEADER)

        if rsp.status_code == 200:
            print(rsp.text)
            rspJson = json.loads(rsp.text.encode())
            if rspJson["status"] == 1:
                return rspJson["resultMap"]
            else:
                print("failed in Moqbus.uiconfig_data_get: status=" + rspJson["status"])
                return None

        else:
            print("failed in Moqbus.uiconfig_data_get: status_code=" + rsp.status_code)
            return None

    @staticmethod
    def calc_ago_time(baseTime):
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