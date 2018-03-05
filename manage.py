# 数据库的初始化，项目的初始化。使用方式参考README.md

# 使用Alembic进行数据库迁移

import os
from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(app=app)


manager.add_command("shell", Shell(make_context=make_shell_context))

if __name__ == '__main__':
    app.run(),  # 切记一定要在此处返回 manager.run()，不然add_command设置的不生效
    # manager.run()
