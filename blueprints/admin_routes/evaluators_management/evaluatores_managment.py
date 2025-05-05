from flask import Blueprint, flash, redirect, render_template, request


bp = Blueprint('evaluators_management', __name__, url_prefix='/admin/evaluators-management')


## search evaluators
@bp.get('/search')
def evaluators_management():
    ''' This function returns the evaluators management page '''

    return render_template('admin/evaluators_management/search.html')

## create evaluators
@bp.get('/create')
def create_evaluator():
    ''' This function returns the create evaluator page '''

    return render_template('admin/evaluators_management/create.html')

## create evaluators post 
@bp.post('/create')
def create_evaluator_post():
    ''' This function creates the evaluator '''

    # get data from form
    email = request.form.get('email')
    name = request.form.get('name')

    # create evaluator
    print("Creating evaluator with email: " + email)
    print("Creating evaluator with name: " + name)
    

    flash("Evaluator created successfully", 'success')

    return render_template('admin/evaluators_management/search.html', )

