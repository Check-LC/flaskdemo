# 这段代码本身在 Python 里是正确的写法。它从当前包的 sqlalchemy 模块导入 db 对象，
# 并通过 __all__ 列表指定当使用 from .extensions import * 时会被导入的对象。
from .sqlalchemy import db
__all__ = ['db']
