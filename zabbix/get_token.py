#!/usr/bin/env python
# encoding=utf-8

import requests
import json
from zabbix import get_api_info

def get_token():
    url = 'http://47.104.186.204:81//zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}

    post_data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": "Admin",
            "password": "zabbixzaq1@WSX"
    },
        "id": 1
    }
    ret = requests.post(url, data=json.dumps(post_data), headers=post_headers)
    return json.loads(ret.text)['result']