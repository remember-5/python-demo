import sqlite3

con = sqlite3.connect("my.db")


def get_con():
    return con


def close():
    con.close()


def create_user():
    """
    创建表格
    """
    cur = con.cursor()
    cur.execute("""create table user
    (
        id     TEXT,
        name   TEXT,
        title  TEXT,
        thumb  TEXT,
        url    TEXT,
        synced INTEGER
    );""")
    # 执行
    con.commit()

    cur.execute("""
    create unique index user__index
        on user (id);
    """)
    con.commit()


def insert_user_data():
    """
    插入数据
    """
    cur = con.cursor()
    cur.execute("""
        INSERT INTO user (id, name, title, thumb, url, synced) VALUES ('2', 'wangjiahao', 'title1', null, null, null);
    """)
    # 执行
    con.commit()


def batch_insert():
    """
    批量插入
    """
    data = [
        ("6", 'wangjiahao', 'title1', None, None, ''),
        ("7", 'wangjiahao', 'title1', None, None, ''),
        ("8", 'wangjiahao', 'title1', None, None, None),
    ]

    cur = con.cursor()
    cur.executemany(
        """
        INSERT INTO user  VALUES(?,?,?,?,?,?)
        """, data)
    con.commit()


def update_user_data():
    pass


def detete_user_data():
    pass


def query_user_data():
    """
    查询数据
    """
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM user;
    """)
    res = cur.fetchall()
    print(res)


if __name__ == '__main__':
    # insert_user_data()
    # batch_insert()
    # query_user_data()
    close()
