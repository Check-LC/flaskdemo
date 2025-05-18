# 下面是一个测试的自定义的过滤器
def datetime_format(value, format='%Y-%m-%d %H:%M'):
    if value is None:
        return ""
    return value.strftime(format)
