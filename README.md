## 使用方式
### 项目运行

- 安装依赖

```
pip install -r requirements.txt
```
- 初始化数据库

```
python manage.py shell //进入shell
from app import db
db.create_all()//初始化数据库
```
- 运行

```
python manage.py runserver
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

## 框架介绍
### Flask-script
> 是一个Flask扩展

```
(flask)$ python manage.py
usage: manage.py [-?] {test,shell,db,runserver} ...

positional arguments:
  {test,shell,db,runserver}
    shell               Runs a Python shell inside Flask application context.
                        (在Flask应用上下文中运行Python shell)
    db                  Perform database migrations
    runserver           Runs the Flask development server i.e. app.run()
                        (运行Flask开发服务器： app.run())

optional arguments:
  -?, --help            show this help message and exit
```
## Flask-Migrate
> 一个网络应用的功能总会不断地发生改变，增加新功能的时候，我们通常需要修改数据库结构。不论你是增删字段还是创建新表，
数据模型的修改会贯穿你的应用开发的始终。但是，当数据库更改变得频繁后，你会很快面临一个问题：当把这些更改从开发环境迁
移到生产环境时，如果不人工对数据模型和对应表的每一行修改进行仔细比较，那么你怎样才能保证所有的更改都会被迁移过去？
又比如，要是你想要把开发环境的代码回滚到Git中的某个历史版本，用来尝试复现目前的生产环境中该版本代码出现的某个问题，
那么你应该怎样把你的数据库结构调整到该版本对应的状态，而无须大量的额外工作呢？
作为程序员，我们痛恨除开发外的额外工作。还好有个工具可以解决这个问题，这个工具是Alembic,可以根据我们的SQLAlchemy
模型的变化，自动创建数据库迁移记录。数据库迁移记录(Database migration)保存了我们的数据库结构变化的历史信息。
Alembic让我们可以把数据库升级或者降级到某个已保存的特定版本，而跨越好几个版本之间的升级或者降级，则会执行这两个选定
版本之间的所有历史记录文件。Alembic最棒的地方在于，这些历史文件本身就是Python程序文件。下面我们创建第1个数据库迁移
记录，你会发现Alembic的语法非常简单。

我们不会直接使用Alembic，而是会使用Flask-Migrate,这是为SQLAlchemy专门创建的一个扩展，

## 提交笔记
- 全局404制定404页面，有api/user和api/article两个基础接口， 根目录返回一个静态的网页。
- 数据库的初始化

## 参考
[数据库+Flask-script+flask_sqlalchemy](http://blog.csdn.net/happyanger6/article/details/53947162)