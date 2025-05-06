import datetime
import io
from flask import Blueprint, flash, redirect, render_template, request, send_file

from blueprints.evaluator_routes.subjects_management.services.subjects_services import search_subjects_service

from blueprints.common.services.question_bank_services import question_bank_service

bp = Blueprint('admin_question_bank', __name__,
               url_prefix='/admin/question-bank')


# search question bank
@bp.get('/search')
def evaluators_management():
    ''' This function returns the evaluators management page '''

    response = question_bank_service.search_question_bank_service()

    if 'error' in response and response['error'] is not None:
        flash(response['message'], 'error')
        return render_template('admin/question_bank/search.html')
    
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

    return render_template('admin/question_bank/search.html', question_banks=question_banks)

@bp.get('/create')
def create_evaluator_get():
    ''' This function returns the create evaluator page '''

    # get all subjects

    subjects = search_subjects_service()

    if 'error' in subjects and subjects['error'] is not None:
        flash(subjects['message'], 'error')
        return render_template('admin/question_bank/create.html')
    
    subjects = subjects['data']

    # map only subjects - code 

    subjects = list(map(lambda x: {
        'code': x.code
    }, subjects))

    return render_template('admin/question_bank/create.html', subjects=subjects)

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
        return render_template('admin/question_bank/create.html')
    
    ## file is only pdf 
    if file.filename == '':
        flash("File is required", 'error')
        return render_template('admin/question_bank/create.html')
    
    if not file.filename.endswith('.pdf'):
        flash("File must be a pdf", 'error')
        return render_template('admin/question_bank/create.html')
    
    file_name = file.filename
    file_data = file.read()

    # convert date to python date object
    try:
        exam_date = datetime.datetime.strptime(
            exam_date, '%d/%m/%Y').date()
    except ValueError:
        flash("Invalid date format", 'error')
        return render_template('admin/question_bank/create.html')
    
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
        return render_template('admin/question_bank/create.html')
    
    # check if response is success

    flash(response['message'], 'success')
    
    return redirect('/admin/question-bank/search')


@bp.get('/approve/<paper_id>')
def approve_evaluator_get(paper_id):
    ''' This function approves the question bank paper '''

    result = question_bank_service.update_status_question_bank_service(paper_id, 'APPROVED')
    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')
        return render_template('admin/question_bank/view.html')

    return redirect('/admin/question-bank/view/' + paper_id)


@bp.get('/reject/<paper_id>')
def reject_evaluator_get(paper_id):
    ''' This function rejects the question bank paper '''

    result = question_bank_service.update_status_question_bank_service(paper_id, 'REJECTED')

    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')
        return render_template('admin/question_bank/view.html')

    return redirect('/admin/question-bank/view/' + paper_id)




@bp.get('/view/<paper_id>')
def update_evaluator_get(paper_id):
    ''' This function returns the create evaluator page '''

    result = question_bank_service.get_question_bank_service(paper_id)

    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')
        return render_template('admin/question_bank/view.html')
    
    question_bank = result['data']

    # map only question banks - code, title, description, subject_code, semester, duration, max_marks, exam_date
    question_bank = {
        'id': question_bank.id,
        'paper_id': question_bank.paper_id,
        'title': question_bank.title,
        'description': question_bank.description,
        'subject_id': question_bank.subject_id,
        'semester': question_bank.semester,
        'duration': question_bank.duration_minutes,
        'max_marks': question_bank.max_marks,
        'exam_date': question_bank.exam_date,
        'status': question_bank.status,
        'file_name': question_bank.file_name,
        'upload_date': question_bank.upload_date,
    }

    return render_template('admin/question_bank/view.html', question_bank=question_bank)

@bp.get('/download/<paper_id>')
def download_evaluator_get(paper_id):
    ''' This function returns the create evaluator page '''

    result = question_bank_service.get_question_bank_service(paper_id)

    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')
        return render_template('admin/question_bank/view.html')
    
    question_bank = result['data']

    file_data = question_bank.file_data
    file_name = question_bank.file_name

    # stream the file
    return (file_data, 200, {
        'Content-Type': 'application/pdf',
        'Content-Disposition': f'attachment; filename={file_name}'
    })

@bp.get('/show-document/<paper_id>')
def show_evaluator_get(paper_id):
    ''' This function returns the create evaluator page '''

    result = question_bank_service.get_question_bank_service(paper_id)

    if 'error' in result and result['error'] is not None:
        flash(result['message'], 'error')
        return render_template('admin/question_bank/view.html')
    
    question_bank = result['data']

    file_data = question_bank.file_data
    file_name = question_bank.file_name

    # stream the file
    return send_file(
        io.BytesIO(file_data),
        mimetype='application/pdf',
        as_attachment=False,
        download_name=file_name
    )