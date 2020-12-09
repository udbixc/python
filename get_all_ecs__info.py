#!/usr/bin/env python
# encoding: utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

client = AcsClient('RPvUL2QtLmHfms45', '2NQHVKTYJq7vrpmk8EbmZdt6Rzbaru', 'cn-qingdao')

request = DescribeInstancesRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
result = str(response, encoding='utf-8')

with open(r'/tmp/.ecs_info.log', 'w', encoding='utf-8') as f:
    f.write(result)

