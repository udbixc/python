#!/usr/bin/env python
#encoding=utf-8

import requests
from zabbix import get_token
import json
from zabbix import get_api_info

def get_hosts():
    post_data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },
        "id": 2,
        "auth": get_token.get_token()
    }

    ret = requests.post(get_api_info.api_info()[0], data=json.dumps(post_data), headers=get_api_info.api_info()[1])
    return json.loads(ret.text)['result']

hosts = get_hosts()
for h in range(0,len(hosts)):
    hostid=json.loads(json.dumps(hosts[h]))["hostid"]
    host=json.loads(json.dumps(hosts[h]))["host"]
    ip=json.loads(json.dumps(hosts[h]))["interfaces"][0]['ip']
    print("hostid>>> ",hostid," host>>> ",host," ip>>> ",ip)