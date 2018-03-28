## 使用方式
### 项目运行

- 安装依赖

```
pip install -r requirements.txt
```

- 运行(如果使用了sql数据库，需要在运行之前初始化数据库)

```
python manage.py runserver
```

## 项目结构
- app 具体业务
  + api 业务逻辑
  + models 数据处理层
  + wraps 装饰器
  + utils 工具类
  + constants.py 常量
- doc 文档
- manage.py 启动
- requirement.txt 依赖

## 提交笔记
- 全局404制定404页面，有api/user和api/article两个基础接口， 根目录返回一个静态的网页。
- 数据库的初始化
- 更改项目结构
- token校验+异常捕获


## api 文档
```
baseUrl: /api/v1
```
### 用户
|地址|类型|详情|token|
|---|---|---|---|
|auth/login|GET|登入|否|

### 文章
|地址|类型|详情|token|
|---|---|---|---|
|/article/list|GET|文章列表|
|/article|GET|文章详情|否|
|/article|POST|创建文章|是|
|/article|PUT|修改文章|是|

### lable
|地址|类型|详情|token|
|---|---|---|---|
|/lable/list|GET|标签列表|否|



## 参考
[数据库+Flask-script+flask_sqlalchemy](http://blog.csdn.net/happyanger6/article/details/53947162)
