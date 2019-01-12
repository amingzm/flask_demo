
SQLALCHEMY_DATABASE_URI = 'mssql+pymssql://sa:123456@127.0.0.1/task'
# 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
SQLALCHEMY_TRACK_MODIFICATIONS = True

'''
import pymssql

conn = pymssql.connect(host='127.0.0.1', user='sa',
                       password='123456', database='task',
                       charset="UTF-8")
# 查看连接是否成功
print(conn)
cursor = conn.cursor()
sql = 'select * from Task1'
cursor.execute(sql)
# 用一个rs变量获取数据
rs = cursor.fetchall()
print(rs)
'''

