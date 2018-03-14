- 初始化数据库(sql类型数据)

```
python manage.py shell //进入shell
from app import db
db.create_all()//初始化数据库
```


### 项目维护
- 数据库的迁移

```
python manage.py db init
//会在项目目录中创建一个叫作migrations的文件夹，所有的记录文件会被保存在里面
python manage.py db migrate
//这个命令会让Alembic扫描我们所有的SQLAlchemy对象，找到在此之前没有被记录过的所有表和列，由于这是第1次提交，所以迁移记录文件会比较大。确保使用了-m参数来保存提交信息，通过提交信息寻找所需的迁移记录版本是最容易的办法。每个迁移记录文件都被保存在migrations/versions/文件夹中。
python manage.py db upgrade
//这个命令，就可以把迁移记录应用到数据库上，并改变数据库的结构：
```