#!/usr/bin/env python
#encoding=utf-8

import requests
import json
import parsel as parsel
import pymysql
import time


def get_proxy(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
    }
    response = requests.get(url=url, headers=header)
    sel = parsel.Selector(response.text)

    # 标识跨节点提取,copy xpath
    ips = sel.xpath('.//table[@class="layui-table"]/tbody/tr/td[1]/text()').getall() #获取ip
    ports = sel.xpath('.//table[@class="layui-table"]/tbody/tr/td[2]/text()').getall() #获取端口

    for ip, port in zip(ips, ports):
        return ip+":"+port

def get_ips(path):
    with open(path, 'r', encoding='utf-8') as f:
        ips = []
        for i, item in enumerate(f.readlines()):
            ips.append((item.split('\n')))
        ip_url = ['http://ip.zxinc.org/api.php?type=json&ip='+str(ip[0]) for ip in ips]
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        }
        url = [u for u in ip_url]
        ip_list = []
        for u in url:
            try:
                proxies = {
                    'http': 'http://{}'.format(get_proxy(url='https://ip.jiangxianli.com')),
                    'https': 'https://{}'.format(get_proxy(url='https://ip.jiangxianli.com'))
                }
                print('使用代理ip: ',get_proxy(url='https://ip.jiangxianli.com'), '爬取ip是：',u.split('ip=')[1])
                response = requests.get(url=u, headers=header, proxies=proxies)
                time.sleep(5)
                response.encoding = 'utf_8_sig'
                data = json.loads(response.text)

                my_ip = u.split('ip=')[1]
                start = data.get('data').get('ip').get('start')
                end = data.get('data').get('ip').get('end')
                area = data.get('data').get('location')
                ip_list.append((my_ip,start,end,area))
            except:
                print("Connection refused by the server..")
                print("Let me sleep for 5 seconds")
                print("ZZzzzz...")
                time.sleep(5)
                print("Was a nice sleep, now let me continue...")
                continue
        return ip_list

result = get_ips(path='ip.txt')

def insert():
    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='ipinfo')

    # 创建游标
    cursor = conn.cursor()
    try:
        sql = "insert into ip(myip,head,tail,area) values(%s,%s,%s,%s)" # 要插入的数据
        cursor.executemany(sql,result) # 执行插入数据
        conn.commit()
        print('insert ok')
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()

def main():
    insert()

main()