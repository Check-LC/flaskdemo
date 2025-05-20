from flask import Blueprint

# 创建蓝图实例，指定蓝图名称和导入名称
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# 从当前包导入 routes 模块，通常 routes 模块包含了该蓝图对应的路由定义
from . import routes

# 定义模块公开的接口，这里表示该模块对外暴露的对象为 auth_bp
# 这个 `__all__` 接口不是必须写的。它的主要作用是定义当使用 `from module import *` 语句时，哪些对象会被导入。
# 对外暴露之后，其他模块可以使用 `from . import *` 语句来导入 `__all__` 列表中指定的对象，例如这里的 `auth_bp`。
# 如果不写 `__all__`，当使用 `from module import *` 时，Python 会导入所有不以下划线开头的全局名称。
__all__ = ['auth_bp']