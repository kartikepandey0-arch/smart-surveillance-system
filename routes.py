from flask import Blueprint, render_template

egov_bp = Blueprint(
    'egov',
    __name__,
    template_folder='templates',
    static_folder='static'
)

@egov_bp.route('/egov')
def egov_home():
    return render_template('login.html')   # your egov template