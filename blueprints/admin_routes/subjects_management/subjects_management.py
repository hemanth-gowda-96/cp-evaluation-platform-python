from flask import Blueprint, render_template


bp = Blueprint('subjects_management', __name__, url_prefix='/admin/subjects-management')

## search evaluators
@bp.get('/search')
def evaluators_management():
    ''' This function returns the evaluators management page '''

    return render_template('admin/subjects_management/search.html')

## create evaluators
@bp.get('/create')
def create_evaluator():
    ''' This function returns the create evaluator page '''

    return render_template('admin/subjects_management/create.html')