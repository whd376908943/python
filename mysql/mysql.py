#!/usr/local/env python
# coding:utf-8
# mysql select


import MySQLdb
conn = MySQLdb.connect(host='192.168.189.128', user='root', passwd='hadoop', db='mydb')
cur = conn.cursor()

sql = 'select tomcat from tomcat '
cur.execute(sql)

# data = cur.fetchmany(2)
# print data
# for i in range(line):
#     data = cur.fetchone()
#    print data
# cur.scroll(0.mode='absolute')
# cur.scroll(1, mode='relative')
data = cur.fetchall()
print data

cur.close()
conn.close()

"""
# mysql update
import MySQLdb
conn = MySQLdb.connect(host='192.168.0.22', user='hadoop', passwd='hadoop', db='mydb')
cursor = conn.cursor()

sql = "update student set age = %s where name = %s"  #%s与参数数据类型无关
parameter = (23, "Li")
cursor.execute(sql, parameter)

conn.commit()
cursor.close()
conn.close()

"""

"""
# mysql insert
import MySQLdb
conn = MySQLdb.connect(host='192.168.0.22', user='hadoop', passwd='hadoop', db='mydb')
cursor = conn.cursor()

sql = 'insert into student values(%s,%s,%s)'
#paramters = [(1, 'He', 25), (3, 'Ha', 27),(4,'My',29)]
parameters = []
for i in range(10, 13, 1):
    parameters.append((i, 'user'+str(i), i+10))
cursor.executemany(sql, parameters)

conn.commit()
cursor.close()
conn.close()
"""

"""
# mysql delete
import MySQLdb
conn = MySQLdb.connect(host='192.168.0.22', user='hadoop', passwd='hadoop', db='mydb')
cursor = conn.cursor()

sql = 'delete from student where age = %s'
parameters = (27,)
cursor.execute(sql, parameters)

conn.commit()
cursor.close()
conn.close()
"""

