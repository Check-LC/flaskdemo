from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import MySQLdb


site = Flask(__name__)

config={ #此处应该需要配置文件
    'HOST':  "mariadb.chaoslong.cn",
    'PORT': "3306",
    'USERNAME': "root",
    'PASSWORD': "gP5X3VfrA",
    'DATABASE': "flask_demo"
}

site.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{config["USERNAME"]}:{config["PASSWORD"]}@{config["HOST"]}:{config["PORT"]}/{config["DATABASE"]}'

db = SQLAlchemy(site)

# 此处在映射中相当于在设计数据库的表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # integer意思是整数，主键+自增
    name = db.Column(db.String(50), nullable=False)  # 最大长度为 50 的字符串字段，对应数据库中的 VARCHAR 类型，不可为空
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Colmun(db.String(200),nullable=False)
    content = db.column(db.Text, nullable=True)

    # 下方是外键;此字段是引用外部表的主键；入库时会受到B表主键约束
    author_id = db.column(db.Integer, db.ForeignKey('user.id')) # 是数据库层面上的外键定义，确保数据一致性。
    author = db.relationship('User', backref='titles')   # 不存在于数据库，仅在 ORM 中有效。还有反向引用
    # backref 会自动给User模型添加一个 titles 的属性

article1 = Article(title='1', content='content of article 1')
# 下方展示关系的逻辑
# author_id = user.id  ==> user = User.query.get(article.author_id) ==> article_author = User.query.get()



with site.app_context():
    db.create_all()