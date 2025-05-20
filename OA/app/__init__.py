from flask import Flask
from config import Config
from app.extensions import db
from app.models import UserModel
from app.blueprints.auth import auth_bp
from app.blueprints.main import main_bp
# from blueprints.api import api_bp

# 称为工厂函数，在创建应用时调用，返回一个应用实例。


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    return app

# 调用 `db.init_app(app)` 的好处在于将数据库实例 `db` 与 Flask 应用 `app` 进行绑定。
# 这种设计实现了数据库实例和应用实例的解耦，使得 `db` 可以在不同的应用中复用。
# 同时，在应用初始化阶段统一配置数据库，方便管理和维护数据库连接等相关设置。
