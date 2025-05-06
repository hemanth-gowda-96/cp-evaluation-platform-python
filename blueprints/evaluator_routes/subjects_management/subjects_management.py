from flask import Blueprint, flash, redirect, render_template, request

from blueprints.evaluator_routes.subjects_management.services import subjects_services

bp = Blueprint('evaluator_subjects_management', __name__,
               url_prefix='/evaluator/subjects-management')


# search evaluators
@bp.get('/search')
def evaluators_management():
    ''' This function returns the evaluators management page '''

    response = subjects_services.search_subjects_service()
    if 'error' in response and response['error'] is not None:
        flash(response['message'], 'error')
        return render_template('evaluator/subjects_management/search.html')

    subjects = response['data']
    if subjects is None:
        flash("No subjects found", 'error')
        return render_template('evaluator/subjects_management/search.html')

    return render_template('evaluator/subjects_management/search.html', subjects=subjects)

@bp.get('/create')
def create_evaluator_get():
    ''' This function returns the create evaluator page '''

    return render_template('evaluator/subjects_management/create.html')


@bp.post('/create')
def create_evaluator():
    ''' This function returns the create evaluator page '''

    # get data from form
    code = request.form.get('code')
    name = request.form.get('name')
    description = request.form.get('description')
    department = request.form.get('department')
    semester = request.form.get('semester')

    print(code, name, description, department, semester)

    # new dict
    subject = {
        'code': code,
        'name': name,
        'description': description,
        'department': department,
        'semester': semester
    }
    result = subjects_services.new_subject(subject)

    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')

        return render_template('evaluator/subjects_management/create.html')

    flash("Subject created successfully", 'success')

    return redirect('/evaluator/subjects-management/search')
