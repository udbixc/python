#!/usr/bin/env python
# encoding utf-8

#判断数据库是否连接成功

from sqlalchemy import create_engine, Column, String, Integer, Index, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'testdbzzzzzzzzzzzzz'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(
    username=USERNAME,
    password=PASSWORD,
    host=HOSTNAME,
    port=PORT,
    db=DATABASE
)
engine = create_engine(DB_URI)

#判断是否连接
try:
    with engine.connect() as conn:
        rs = conn.execute('select 1')
        print(rs.fetchone())
except Exception as e:
    print(e)