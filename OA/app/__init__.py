from flask import Flask
from config import Config
from app.factory import _create_app

# 仅保留核心导入和工厂函数调用
# 称为工厂函数，在创建应用时调用，返回一个应用实例。
def create_app():
      # 从单独文件导入工厂函数
# 这里返回 _create_app() 是因为 _create_app 是从单独文件导入的工厂函数，
# 工厂函数的作用是在创建应用时调用并返回一个应用实例，
# 所以通过返回 _create_app() 可以得到创建好的应用实例。
    return _create_app()

