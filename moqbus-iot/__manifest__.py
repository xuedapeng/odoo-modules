# -*- coding: utf-8 -*-
{
    'name': "moqbus-物联设备111",

    'summary': """
        为moqbus物联网平台提供一个友好的前端操作界面 222 
     """,

    'description': """
        包括组态管理、气象站显示与控制、电动阀的显示与控制等。
    """,

    'author': "xuedapeng",
    'website': "http://doc.moqbus.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Manufacturing',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/config.xml',
        'views/device.xml',
        'views/sensor_qxz.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ]
}
