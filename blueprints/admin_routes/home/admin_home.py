''' admin_routes/home/home.py '''
from flask import (
    Blueprint, render_template
)


bp = Blueprint('admin_home', __name__, url_prefix='/admin/home')


@bp.get('/')
def home():
    ''' This function returns the home page '''

    return render_template('admin/home.html')
