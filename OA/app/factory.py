from flask import Flask
from config import Config
from app.extensions import db
from app.models import UserModel
from app.blueprints.auth import auth_bp
from app.blueprints.main import main_bp
from flask_migrate import Migrate  # 设计好Model后，需要执行迁移命令，将Model映射到数据库中。
# 先进入虚拟环境，然后进行flask db init，再进行flask db migrate -m "message"，再进行flask db upgrade。


def _create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # 加载配置
    db.init_app(app)
    migrate = Migrate(app, db)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    return app

# 调用 `db.init_app(app)` 的好处在于。
# 这种设计实现了数据库实例和应用实例的解耦，使得 `db` 可以在不同的应用中复用。
# 同时，在应用初始化阶段统一配置数据库，方便管理和维护数据库连接等相关设置。
'''
      1.  db.init_app(app) 将数据库实例 `db` 与 Flask 应用 `app` 进行绑定；会从 app.config 中读取 SQLALCHEMY_DATABASE_URI，并使用它创建数据库连接池（底层调用 mysqlclient 或其他 MySQL 驱动）
      2.  当模型（models.py 中的 SQLAlchemy 模型）发生变化时，运行 flask db migrate -m "message" 会检测模型与当前数据库的差异，生成一个迁移脚本（Python 文件，存放在 migrations/versions/ 目录下）。迁移脚本包含升级（upgrade()）和降级（downgrade()）操作，分别用于应用变更和回滚变更。
# migrate = Migrate(app, db)
    # 创建一个 Migrate 实例，将 Flask 应用 `app` 和 SQLAlchemy 数据库实例 `db` 关联起来。并可以管理其Model变化, 用于db数据库的迁移.
    # 可以使用 Flask-Migrate 提供的命令（如 `flask db migrate` 和 `flask db upgrade`）来管理数据库迁移，
    # 自动生成迁移脚本并将模型的变更应用到数据库中，方便数据库的版本控制和升级。
'''