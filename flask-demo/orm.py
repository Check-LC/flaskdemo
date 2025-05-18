# ORM 映射数据库   
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

# with site.app_context():
#     try:
#         with db.engine.connect() as conn:
#             rs = conn.execute(text('show databases'))
#             print(rs.fetchall())
#     except Exception as e:
#         print(f"数据库连接失败: {str(e)}")
'''
ORM 对象关系映射
1. 效率高，不需要原生SQL语句
2. 安全性、灵活性
3. 常见的ORM框架
Java：Hibernate、MyBatis
Python：Django ORM、SQLAlchemy
JavaScript（Node.js）：Sequelize

Python 类型 (db.Column)	数据库类型	描述
db.Integer	INT	整数，如 1, 2, -5, 100
db.String(50)	VARCHAR(50)	可变长度字符串
db.Text	TEXT	长文本内容
db.Boolean	BOOLEAN	布尔值（True/False）
db.DateTime	DATETIME	日期和时间
db.Float	FLOAT	浮点数，如 3.14
db.Numeric(precision, scale)	DECIMAL(precision, scale)
'''

# 此处在映射中相当于在设计数据库的表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # integer意思是整数，主键+自增
    name = db.Column(db.String(50), nullable=False)  # 最大长度为 50 的字符串字段，对应数据库中的 VARCHAR 类型，不可为空
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)

# user = User(name="john", email="john@example.com", password="passwordofjohn")

with site.app_context():
    db.create_all()


@site.route('/')
def index():
    return 'hello world'

@site.route('/user/add')
def add_user(): # Flask  视图函数（即路由处理函数）必须返回一个响应，
    user = User(name="john", email="john@example.com", password="passwordofjohn") # 实例化ORM对象，输入用户信息
    db.session.add(user)  # 增加到数据库会话
    db.session.commit()   # 提交到数据库
    return 'user added'

@site.route('/user/query')
def  query_user():
    # 1. 通过主键 get
    # user = User.query.get(1)  # 在User类(表)中查找主键1的一条记录
    # 2. filter
    user = User.query.filter(User.name == 'john').first()
    return f"{user.email} finded"

@site.route('/user/update')
def update_user():
    user = User.query.filter(User.name == 'john').first()
    user.email = 'john@qq.com'
    db.session.commit()
    return f"{user.email} updated"

@site.route('/user/delete')
def delete_user():
    user = User.query.filter(User.name == 'john').first()
    db.session.delete(user)
    db.session.commit()
    return f"{user.name} deleted"


if __name__  == '__main__':
    site.run(port=80, debug=True)