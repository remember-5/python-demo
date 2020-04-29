import mysql.connector

# 打开数据库连接
db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    passwd='root',
    database='pydb',
)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = '''
    SELECT * FROM t_user
    '''
cursor.execute(sql)
# 使用 fetchall() 方法获取s所有数据
data = cursor.fetchall()

print(data)
# 关闭数据库连接
db.close









