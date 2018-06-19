# -*- coding: utf-8 -*-
#第17章Scrapy高级应用
#17.1 Python3如何操作数据库
import pymysql.cursors
import pymysql
# conn=pymysql.connect(host="127.0.0.1", user="root", passwd="198@7BoY")
# conn.query("create database mypydb1")
#conn=pymysql.connect(host="127.0.0.1", user="root", passwd="198@7BoY", db="mypydb",charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#conn=pymysql.connect(host="127.0.0.1", user="root", passwd="198@7BoY", db="mypydb",charset='utf8', cursorclass=pymysql.cursors.DictCursor)
#conn=pymysql.connect(host="127.0.0.1", user="root", passwd="198@7BoY", db="mypydb",cursorclass=pymysql.cursors.DictCursor)
conn=pymysql.connect(host="127.0.0.1", user="root", passwd="198@7BoY", db="mypydb")
#conn.query("CREATE TABLE mytb(title VARCHAR(255) COLLATE utf8_bin NOT NULL,keywd VARCHAR(255) COLLATE utf8_bin) ENGINE=INNODB DEFAULT CHARSET=utf8 COLLATE=utf8_bin")
#conn.query("CREATE TABLE mytb(title VARCHAR(255) NOT NULL,keywd VARCHAR(255))")
cs=conn.cursor()
a='生2命'
b='安1全'
sql="insert into mytb(title,keywd) VALUES('"+a+"','"+b+"')"
cs.execute(sql)
# 提交SQL
conn.commit()#至关重要
cs.execute("select * from mytb")
result=cs.fetchone()
print(result)
print("-----------华丽分割线------------")

# 执行数据查询
cs.execute("select * from mytb")

#查询数据库多条数据
result = cs.fetchall()
for data in result:
    print(data)


# 关闭数据连接
conn.close()