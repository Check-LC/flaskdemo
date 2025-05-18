from flask import Flask, render_template, request
from utils.test_utils import datetime_format
from datetime import datetime
import mysqlclient
from flask_sqlalchemy import SQLAlchemy

site = Flask(__name__)


class User:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email


@site.route("/")
def root():
    return "Hello from root of flask-demo! day2"


@site.route("/route/list")
def route_list():
    page = request.args.get("page", type=int, default=1)
    return f"route_list page {page}"


@site.route("/greet")
def greet():
    HumanKind = User("man1", 1, "man1@qq.com")
    return render_template("hello.html", info=HumanKind)

# @site.route("/blog")
# def route_blog():
#     return render_template("blog.html")


@site.route("/blog/<pid>")
def route_subblog(pid):
    # return render_template("hello.html", tvar="localvars")
    return render_template("blog.html", page=pid)


# 过滤器示例
site.add_template_filter(datetime_format, "dt_format")


@site.route("/filter")
def route_filter():
    # 报错原因可能是没有导入 datetime 模块，下面添加导入语句并修正代码
    time_now = datetime.now()
    return render_template("filter.html", time=time_now)


@site.route("/control/<username>")
def route_control(username):
    return render_template("control.html", username=username)

# 模板继承


@site.route("/child")
def route_child():
    return render_template("child.html")

# 加载静态资源


@site.route("/statics")
def route_static():
    return render_template("statics.html")


if __name__ == "__main__":
    site.run(host='0.0.0.0', port=80, debug=True)

'''
1. debug 模式便于调试，实时渲染
To bind to a specific IP and port, you can pass them as arguments to the run method.
    # By default, Flask runs on 127.0.0.1:5000. To make it publicly available, use 0.0.0.0.
    # For example, to bind to all available IPs on port 8080:
    # site.run(host='0.0.0.0', port=8080, debug=True)
'''
