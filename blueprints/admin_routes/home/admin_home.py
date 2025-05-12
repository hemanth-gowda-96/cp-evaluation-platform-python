''' admin_routes/home/home.py '''
from flask import (
    Blueprint, flash, render_template
)

from blueprints.admin_routes.home.services.dashboard_services import get_dashboard_data


bp = Blueprint('admin_home', __name__, url_prefix='/admin/home')


@bp.get('/')
def home():
    ''' This function returns the home page '''

    result = get_dashboard_data()

    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')

        return render_template('admin/home.html')
    
    data = result['data']
    count_cards = data['count_cards']
    total_questions_per_subject = data['total_questions_per_subject']

    print(count_cards)
    print(total_questions_per_subject)
    

    return render_template('admin/home.html', count_cards=count_cards
                            , total_questions_per_subject=total_questions_per_subject
    )
