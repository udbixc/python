#!/usr/bin/env python
#encoding=utf-8

data = {"hostid": "10084", "host": "Zabbix server", "interfaces": [{"interfaceid": "1", "ip": "127.0.0.1"}]}
#print(type(data))

#print(data['host'])

host={"hostid": "10084", "host": "Zabbix server", "interfaces": [{"interfaceid": "1", "ip": "127.0.0.1"}]}
print(host["host"])