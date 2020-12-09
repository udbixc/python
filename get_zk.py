#!/usr/bin/python

import socket
#from StringIO import StringIO
from cStringIO import StringIO
s=socket.socket()

s.connect(('localhost',2181))
s.send('mntr')
data_mntr=s.recv(2048)
s.close()
#print data_mntr
h=StringIO(data_mntr)
result={}
zresult={}
for line in  h.readlines():
  key,value=map(str.strip,line.split('\t'))
  zkey='zookeeper.status' + '[' + key + ']'
  zvalue=value
  result[key]=value
  zresult[zkey]=zvalue
print result
print '\n\n'
print zresult
