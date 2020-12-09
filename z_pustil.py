#!/usr/bin/env python
#
#encoding utf-8


import psutil
from datetime import datetime

#查看磁盘分区
#
#disks = psutil.disk_partitions()
#for disk in disks:
#    print(disk)

print('\n')

#磁盘使用率
#
disks = psutil.disk_partitions()
for disk in disks:
    print(disk.device, psutil.disk_usage(disk.device))

print('\n')

#查看磁盘的io
#
io = psutil.disk_io_counters()
print('磁盘IO:', io)
print('数据类型:', type(io), '\n')

#获取运行时间
#print(psutil.boot_time())
#
print("开机时间是")
print(datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H: %M: %S"))
print('\n')

#获取cpu信息
#
#cpu完成信息
#print(psutil.cpu_times())
#
#print('\n')

#cpu逻辑个数
print("cpu逻辑个数是")
print(psutil.cpu_count())
print('\n')

#cpu使用率
print("cpu的使用率是")
print(psutil.cpu_percent())
print('\n')

mem = psutil.virtual_memory()
#print(mem)
#print('\n')

#获取内存信息
#
print("可用内存是 "+str(mem.total/1024/1024)+" M")
print('\n')

#print("总共内存是："+str(mem.total))
#print('\n')

print("使用内存是："+str(mem.used))
print('\n')

print("空存内存是："+str(mem.free))
print('\n')
#获取系统进程信息

print("运行的应用有这些")
for pid in psutil.pids():
    p = psutil.Process(pid)
    print(p.name())
#    print(p.as_dict())