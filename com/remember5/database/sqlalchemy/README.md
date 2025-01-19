# SQLAlchemy
```shell
pip install SQLAlchemy
```



# alembic 版本管理
安装
```shell
pip install alembic
```

新建版本
```shell
alembic revision -m "create account table"
```

更新版本
```shell
alembic upgrade head
```


# Flask-SQLAlchemy

## 创建迁移版本
自动创建迁移版本有两个函数  
upgrade()：函数把迁移中的改动应用到数据库中。  
downgrade()：函数则将改动删除。  
自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，生成upgrade()和downgrade()函数的内容。  
对比不一定完全正确，有可能会遗漏一些细节，需要进行检查  

```shell
flask db migrate -m 'initial migration'
```


## 升级版本库的版本
```shell
# 从migations目录下的versions中根据迁移文件upgrade方法把数据表的结构同步到数据库中。
flask db upgrade
```

## 降级版本库的版本

```shell
# 从migations目录下的versions中根据迁移文件downgrade把数据表的结构同步到数据库中。
python main.py db downgrade
```

## 版本库的历史管理
可以根据history命令找到版本号,然后传给downgrade命令:

```shell
python manage.py db history

输出格式：<base> ->  版本号 (head), initial migration
```
回滚到指定版本

```shell
flask db downgrade # 默认返回上一个版本
flask db downgrade 版本号   # 回滚到指定版本号对应的版本
flask db upgrade 版本号     # 升级到指定版本号对应的版本

```

数据迁移的步骤：

```shell
1. 初始化数据迁移的目录
export FLASK_APP=manage.py
flask db init

2. 数据库的数据迁移版本初始化
flask db migrate -m 'initial migration'

3. 升级版本[创建表/创建字段/修改字段]
flask db upgrade 

4. 降级版本[删除表/删除字段/恢复字段]
flask db downgrade

```

# sqlacodegen model 生成

https://github.com/agronholm/sqlacodegen


# 参考
- https://www.cnblogs.com/hsqKTm/p/14821303.html
