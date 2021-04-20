#!/usr/bin/env python
#encoding=utf-8

def api_info():
    url = 'http://47.104.186.204:81//zabbix/api_jsonrpc.php'
    post_headers = {'Content-Type': 'application/json'}
    return url,post_headers