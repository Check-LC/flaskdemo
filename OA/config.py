# config.py
import os
from configparser import ConfigParser

# 读取 oa.conf 配置文件
config = ConfigParser()
if not os.path.exists('oa.conf'):
    raise FileNotFoundError("配置文件 oa.conf 不存在，请创建")

config.read('oa.conf', encoding='utf-8')

# 从 [app] 分组中提取数据库配置项
try:
    db_config = {
        'driver': config.get('app', 'DATABASE_DRIVER'),
        'user': config.get('app', 'DATABASE_USER'),
        'password': config.get('app', 'DATABASE_PASSWORD'),
        'host': config.get('app', 'DATABASE_HOST'),
        'port': config.getint('app', 'DATABASE_PORT'),
        'dbname': config.get('app', 'DATABASE_NAME')
    }
except Exception as e:
    raise ValueError(f"缺失必要配置项: {str(e)}")

# 拼接完整的数据库 URI
# 错误提示表明 db_config 可能不是预期的字典类型，这里假设 db_config 是字典，检查键是否存在
SQLALCHEMY_DATABASE_URI = f"{db_config['driver']}://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"



class Config:
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    DEBUG = config.getboolean('app', 'DEBUG', fallback=False)
    # getboolean 方法用于从配置文件中获取指定 section 和 option 的布尔值。
    # 第一个参数 'app' 表示配置文件中的 section 名称，即配置项所属的分组。
    # 第二个参数 'DEBUG' 表示要获取的配置项的名称。
    # 第三个参数 fallback=False 是一个可选参数，当指定的 section 和 option 不存在时，会返回该默认布尔值
    SQLALCHEMY_TRACK_MODIFICATIONS = False
