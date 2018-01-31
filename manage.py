# 数据库的初始化，项目的初始化。使用方式参考README.md

# 使用Alembic进行数据库迁移

import os
from app import create_app, db
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app.models import User

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

migrate = Migrate(app, db)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    # app.run(),  # 切记一定要在此处返回 manager.run()，不然add_command设置的不生效
    manager.run()
