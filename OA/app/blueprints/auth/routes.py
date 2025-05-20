from . import auth_bp

@auth_bp.route('/login')
def login():
# 在Flask里，render_template默认会从templates目录下寻找模板文件。
# 所以'auth/login.html' 应该放在templates目录下的auth子目录中，而非static目录。
# static目录主要用于存放静态文件，如CSS、JavaScript、图片等。
  return render_template('auth/login.html')
