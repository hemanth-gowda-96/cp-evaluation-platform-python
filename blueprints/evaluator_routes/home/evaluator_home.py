''' admin_routes/home/home.py '''
from flask import (
    Blueprint, render_template
)


bp = Blueprint('evaluator_home', __name__, url_prefix='/evaluator/home')


@bp.get('/')
def home():
    ''' This function returns the home page '''

    return render_template('evaluator/home.html')
