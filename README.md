## 学习笔记
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


## 提交笔记
第一版   全局404制定404页面，有api/user和api/article两个基础接口， 根目录返回一个静态的网页。