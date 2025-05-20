# 定义数据库模型
from app.extensions import db

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
