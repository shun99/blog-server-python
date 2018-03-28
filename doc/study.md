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

## 字典，对象，json，json字符串
```
字典和json类似，但是字典的key比json的key范围大，json字符串是指json两边带有引号的一个字符串，通常情况下可以很方便的转化为json
```

#### 字典与对象的取值方式
```
args['id'] 和 args.get('id')
当字典args不要存在id时，第一种报错，第二种不报错

对象article取值  article.id

```


## 疑问
### python manage.py runserver的方式启动app的时候执行两次
原因是：在开发模式下，通过python manage.py runserver的方式启动app的时候，会启动两个线程去加载settings文件，
一个是用来给你服务的，另一个是监控settings文件是否改变的。