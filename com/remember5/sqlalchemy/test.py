from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from sqlalchemy import Boolean, Column, Integer, String

# 创建engine，即数据库驱动信息
engine = create_engine(
    url='sqlite:///sqlite-test.db',  # 定义数据库路径（不存在会自动创建）
    echo=True,  # echo 设为 True 会打印出实际执行的 sql，调试的时候更方便
    future=True,  # 使用 SQLAlchemy 2.0 API，向后兼容
    pool_size=5,  # 连接池的大小默认为 5 个，设置为 0 时表示连接无限制
    pool_recycle=3600,  # 设置时间以限制数据库自动断开
    connect_args={
        'check_same_thread': False  # 是否多线程 必须加上 check_same_thread=False，否则无法在多线程中使用
    }
)

# 创建session类对象（建立和数据库的链接）
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# 创建基类
class Base(DeclarativeBase):
    pass


# 定义User表结构
class User(Base):
    # User类对象对应表users
    __tablename__ = 'users'
    my_id = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name = mapped_column(String(32), unique=True, index=True)
    passwd = mapped_column(String(32), index=True)
    is_active = mapped_column(Boolean, default=True)


# 创建表
# checkfirst=True 默认也是 True，即如果数据库存在则不再创建
Base.metadata.create_all(engine, checkfirst=True)


def crud():
    # https://hellowac.github.io/technology/python/sqlalchemy/
    # 创建session实例（实例化）
    db = SessionLocal()

    db.add(User(
        name='Frank',
        passwd='pwd@123'
    ))
    # 提交后才算正式插入数据
    db.commit()

    # 查询数据
    res = db.query(User).all()
    print(res)

    # 条件查询
    user1 = db.query(User).filter_by(my_id=1).first()
    print(user1)
    # 更新
    user1.name = 'Frank1'
    db.commit()

    # 查询
    user2 = db.query(User).filter_by(my_id=1).first()
    print(user2)

    # 关闭数据库连接
    db.close()


if __name__ == '__main__':
    crud()
