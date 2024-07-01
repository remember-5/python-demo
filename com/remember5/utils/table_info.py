from datetime import datetime

import mysql.connector
import pandas as pd

# 连接 MySQL 数据库
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456",
    database="testdb"
)

# 获取数据库游标
cursor = db.cursor()

# 查询所有表名
cursor.execute("""
    SELECT 
        TABLE_NAME
    FROM 
        information_schema.TABLES
    WHERE 
        TABLE_SCHEMA = %s
""", (db.database,))
tables = cursor.fetchall()

# 创建一个空列表,用于存储所有表的字段信息
all_columns = []

# 遍历所有表,查询字段信息
for table in tables:
    table_name = table[0]

    # 查询表字段信息
    cursor.execute("""
        SELECT 
            COLUMN_NAME, 
            COLUMN_TYPE, 
            IS_NULLABLE, 
            COLUMN_DEFAULT, 
            COLUMN_COMMENT
        FROM 
            information_schema.COLUMNS
        WHERE 
            TABLE_NAME = %s 
            AND TABLE_SCHEMA = %s
    """, (table_name, db.database))
    columns = cursor.fetchall()

    # 将当前表的字段信息添加到all_columns列表
    for column in columns:
        column_name = column[0]
        column_type = column[1]
        is_nullable = column[2]
        column_default = column[3] if column[3] is not None else ""
        column_comment = column[4] if column[4] is not None else ""
        all_columns.append({
            "Table": table_name,
            "Field": column_name,
            "Type": column_type,
            "Null": is_nullable,
            "Default": column_default,
            "Comment": column_comment
        })

# 将all_columns列表转换为pandas DataFrame
df = pd.DataFrame(all_columns)

# 获取当前时间戳
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# 将DataFrame保存到Excel文件,文件名包含时间戳
file_name = f"database_schema_{timestamp}.xlsx"
df.to_excel(file_name, index=False)

# 关闭数据库连接
db.close()

print("Database schema saved to 'database_schema.xlsx'")
