from flask import Blueprint, flash, redirect, render_template, request, url_for

from blueprints.admin_routes.evaluators_management.services import evaluators_services

bp = Blueprint('evaluators_management', __name__,
               url_prefix='/admin/evaluators-management')


# search evaluators
@bp.get('/search')
def evaluators_management():
    ''' This function returns the evaluators management page '''

    response = evaluators_services.search_evaluvators_service()

    if 'error' in response and response['error'] is not None:
        flash(response['message'], 'error')
        return render_template('admin/evaluators_management/search.html')

    evaluators = response['data']
    if evaluators is None:
        flash("No evaluators found", 'error')
        return render_template('admin/evaluators_management/search.html')

    # render the page with the evaluators
    return render_template('admin/evaluators_management/search.html', evaluators=evaluators)

# create evaluators


@bp.get('/create')
def create_evaluator():
    ''' This function returns the create evaluator page '''

    return render_template('admin/evaluators_management/create.html')

# create evaluators post


@bp.post('/create')
def create_evaluator_post():
    ''' This function creates the evaluator '''

    # get data from form
    email = request.form.get('email')
    name = request.form.get('name')
    department = request.form.get('department')
    designation = request.form.get('designation')
    phone_number = request.form.get('phone_number')

    result = evaluators_services.new_evaluator(email, name, department=department, designation=designation,
                                               phone_number=phone_number)
    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')
        return render_template('admin/evaluators_management/create.html')

    flash("Evaluator created successfully", 'success')

    return redirect(url_for('evaluators_management.evaluators_management'))
