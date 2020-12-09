# encoding: utf-8


import psutil

#获取当前用户登入数量
from psutil._common import bytes2human

login_users = len(psutil.users())

#获取cpu信息
def get_cpu():
    #cpu实例数量
    cpu_count = len(psutil.Process().cpu_affinity())

    #每颗cpu的物理核心数
    cpu_py_count = psutil.cpu_count(logical=False)

    #cpu信息
    cpu_info = psutil.cpu_times_percent(interval=0.1)

    return cpu_count, cpu_py_count, cpu_info

def display_cpu():
    cpu_temple = """
###############Cpu_Info#################
cpu颗数: {cpu_count}
cpu总使用率: {cpu_time}%
物理核心数: {cpu_py_count}
io等待cpu空闲率: {io_wait_time}%    
    """

    cpu_count, cpu_py_count, cpu_info = get_cpu()
    import sys
    plf = sys.platform
    print(cpu_temple.format(
        cpu_count=cpu_count,
        cpu_py_count=cpu_py_count,
        cpu_time=cpu_info.user + cpu_info.system,
        io_wait_time=cpu_info.iowait if plf == 'linux' else ''
    ))

def get_mem():
    #内存信息
    return psutil.virtual_memory()

def display_mem():
    mem_info = get_mem()
    print("*" * 16, "Disk 信息", "*" * 16)
    fileds = ['tptal', 'free', 'used']
    for name in mem_info._fields:
        if name in fileds:
            value = getattr(mem_info, name)
            value = bytes2human(value)
            print("{:<10s} : {}".format(name.capitalize(), value))

def get_disk_part():
    return psutil.disk_partitions(all=False)

def display_disk():
    disk_fields = ("Device", "Total", "Used", "Free", "Usage", "Type", "Type")
    temple_title = '{:<23s} {:<8} {:<8} {:<8} {:<3s}% {:>8s} {:<s}'
    temple = '{:<23s} {:<8} {:<8} {:<8} {:<3f}% {:>8s} {:<s}'

    disk_part = get_disk_part()
    disk_detail = temple_title.format(*disk_fields)

    print("*" * 35, "Disk 信息", "*" * 35)
    print(disk_detail)

    for part in disk_part:
        #获取磁盘利用率
        usage = psutil.disk_usage(part.mountpoint)

        print(temple.format(
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            usage.percent,
            part.fstype,
            part.mountpoint
        ))

def get_net_info():
    import socket
    net_info_dic = {}
    if_stats_dic = psutil.net_if_stats()
    if_addrs_dic = psutil.net_if_addrs()
    io_counters_obj = psutil.net_io_counters()

    for nic, addrs in if_addrs_dic.items():
        if not nic.startswitch('lo'):
            net_info_dic[nic] = {'nic_stat': if_stats_dic[nic].isup}
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    net_info_dic[nic].update(
                        {
                            'ip': addr.address,
                            'netmask': addr.netmask
                        }
                    )

    for item in net_info_dic.values():
        item.setdefault('ip', '')
        item.setdefault('netmask', '')

    net_info_dic['io_info'] = {
        'bytes_sent': bytes2human(io_counters_obj.bytes_sent),
        'bytes_recv': bytes2human(io_counters_obj.bytes_recv),
        'packe_sent': io_counters_obj.packets_sent,
        'packe_recv': io_counters_obj.packets_recv,
    }

    return net_info_dic

def display_net():
    net_info_dic = get_net_info()
    print(net_info_dic)
    temple_addr = """
        网卡名： {nic}
        状态： {stat}
        IP： {ip}
        掩码： {net_mask}
    """

    temple_io  = """
        当前系统网络IO信息
        当前发送字节数： {bytes_sent}
        当前接收字节数： {bytes_recv}
    """
    print("*" * 30, "Network信息", "*" * 30)
    print(temple_io.format(
        bytes_sent=net_info_dic['io_info'].get('bytes_sent', ''),
        bytes_rent=net_info_dic['io_info'].get('bytes_rent', '')
    ))
    net_info_dic.pop('io_info')

    for nic, item in net_info_dic.items():
        print(temple_addr.format(
            nic=nic,
            stat=item['nic_stat'],
            ip=item.get('ip', ''),
            net_mask=item.get('netmask', '')
                                 ))

def man():
    import sys
    display_dic = {
        "1": {"title": "查看CPU信息", "func": display_cpu()},
        "2": {"title": "查看Memory信息", "func": display_mem()},
        "3": {"title": "查看Disk信息", "func": display_disk()},
        "4": {"title": "查看Network信息", "func": display_net()},
    }

    print("{}Os信息收集".format('*' * 10))
    for k, item in display_dic.items():
        print(k, item['title'])
    while True:
        inp = input("请选择》》：")
        if inp == 'q':
            sys.exit("退出")
        if inp in display_dic.keys():
            print(f"{'*' * 10}emmmmmmm")
            print("{}".format('*' * 10))
            for k, item in display_dic.items():
                print(k, item['title'])
            print()
            exec_func = display_dic[inp]['func']
            exec_func()
            print()

if __name__ == '__main__':
    man()