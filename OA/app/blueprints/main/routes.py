from . import main_bp

@main_bp.route('/')
@main_bp.route('/index')
def index():
    return render_template('main/index.html')
