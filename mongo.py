# MongoDB的demo
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://localhost:27017/blog',
)
mongo = PyMongo()
mongo.init_app(app)


# user = {'name': 'Michael', 'age': 18, 'scores': [{'course': 'Math', 'score': 76}]}
# mongo.db.users.insert(user)
# ======  error =====  数据库的操作不能放在app.run()之前，否则报如下错误
# This typically means that you attempted to use functionality that needed
# to interface with the current application object in a way.  To solve
# this set up an application context with app.app_context().  See the
# documentation for more information.


@app.route('/')
def hello():
    user = {'name': 'Michael', 'age': 18, 'scores': [{'course': 'Math', 'score': 76}]}
    mongo.db.users.insert(user)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
