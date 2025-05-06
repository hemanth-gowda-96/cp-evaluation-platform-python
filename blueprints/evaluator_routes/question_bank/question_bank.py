from flask import Blueprint, flash, render_template, request

from blueprints.evaluator_routes.subjects_management.services.subjects_services import search_subjects_service


bp = Blueprint('evaluator_question_bank', __name__,
               url_prefix='/evaluator/question-bank')


# search question bank
@bp.get('/search')
def evaluators_management():
    ''' This function returns the evaluators management page '''

    # response = subjects_services.search_subjects_service()
    # if 'error' in response and response['error'] is not None:
    #     flash(response['message'], 'error')
    #     return render_template('evaluator/subjects_management/search.html')

    # subjects = response['data']
    # if subjects is None:
    #     flash("No subjects found", 'error')
    #     return render_template('evaluator/subjects_management/search.html')

    return render_template('evaluator/question_bank/search.html')

@bp.get('/create')
def create_evaluator_get():
    ''' This function returns the create evaluator page '''

    # get all subjects

    subjects = search_subjects_service()

    if 'error' in subjects and subjects['error'] is not None:
        flash(subjects['message'], 'error')
        return render_template('evaluator/question_bank/create.html')
    
    subjects = subjects['data']

    # map only subjects - code 

    subjects = list(map(lambda x: {
        'code': x.code
    }, subjects))

    return render_template('evaluator/question_bank/create.html', subjects=subjects)

@bp.post('/create')
def create_evaluator_post():
    ''' This function returns the create evaluator page '''

    code = request.form.get('code')
    title = request.form.get('title')
    description = request.form.get('description')
    subject_code = request.form.get('subject_code')
    semester = request.form.get('semester')
    duration = request.form.get('duration')
    max_marks = request.form.get('max_marks')
    exam_date = request.form.get('exam_date')

    print(code, title, description, subject_code,
          semester, duration, max_marks, exam_date)
    
    return render_template('evaluator/question_bank/create.html')