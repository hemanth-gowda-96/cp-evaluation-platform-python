import datetime
from flask import Blueprint, flash, redirect, render_template, request

from blueprints.evaluator_routes.subjects_management.services.subjects_services import search_subjects_service

from blueprints.common.services.question_bank_services import question_bank_service

bp = Blueprint('evaluator_question_bank', __name__,
               url_prefix='/evaluator/question-bank')


# search question bank
@bp.get('/search')
def evaluators_management():
    ''' This function returns the evaluators management page '''

    response = question_bank_service.search_question_bank_service()

    if 'error' in response and response['error'] is not None:
        flash(response['message'], 'error')
        return render_template('evaluator/question_bank/search.html')
    
    question_banks = response['data']

    # map only question banks - code, title, description, subject_code, semester, duration, max_marks, exam_date
    question_banks = list(map(lambda x: {
        'paper_id': x.paper_id,
        'title': x.title,
        'description': x.description,
        'subject_id': x.subject_id,
        'semester': x.semester,
        'duration': x.duration_minutes,
        'max_marks': x.max_marks,
        'exam_date': x.exam_date,
        'status': x.status
    }, question_banks))

    flash(response['message'], 'success')

    return render_template('evaluator/question_bank/search.html', question_banks=question_banks)

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
    file = request.files.get('file')

    # check if file exists
    if file is None:
        flash("File is required", 'error')
        return render_template('evaluator/question_bank/create.html')
    
    file_name = file.filename
    file_data = file.read()

    # convert date to python date object
    try:
        exam_date = datetime.datetime.strptime(
            exam_date, '%d/%m/%Y').date()
    except ValueError:
        flash("Invalid date format", 'error')
        return render_template('evaluator/question_bank/create.html')
    
    # create dict for all required fields
    required_fields = {
        'code': code,
        'title': title,
        'description': description,
        'subject_code': subject_code,
        'semester': semester,
        'duration': duration,
        'max_marks': max_marks,
        'exam_date': exam_date,
        'file_name': file_name,
        'file_data': file_data
    }
    

    response = question_bank_service.create_new_question_bank_service(
        required_fields)
    if 'error' in response and response['error'] is not None:
        flash(response['message'], 'error')
        return render_template('evaluator/question_bank/create.html')
    
    # check if response is success

    flash(response['message'], 'success')
    
    return redirect('/evaluator/question-bank/search')