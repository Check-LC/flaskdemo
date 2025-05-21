# 定义数据库模型
from app.extensions import db
from datetime import datetime as Datetime

# 映射为表，创建好后使用 flask migrate 工具将其映射到数据库
class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
# 原代码中 db.D 应为 db.DateTime，datetime 应为导入的 Datetime
    create_time = db.Column(db.DateTime, default=Datetime.now)
