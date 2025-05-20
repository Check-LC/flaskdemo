from flask import Blueprint

# 创建蓝图实例，指定蓝图名称和导入名称
main_bp = Blueprint('main', __name__, url_prefix='/')

# 从当前包导入 routes 模块，通常 routes 模块包含了该蓝图对应的路由定义
# 这种导入方式可能会导致循环引用问题，因为如果 routes 文件中导入了 main_bp，
# 就会形成循环依赖。为了避免这种情况，可以在函数内部延迟导入，
# 或者调整代码结构以避免相互依赖。
from . import routes