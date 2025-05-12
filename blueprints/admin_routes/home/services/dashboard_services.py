
import random
from sqlalchemy import func
from db.models import QuestionPaper, Subject, User
from db.models import db

def get_dashboard_data():
    ''' This function returns the dashboard data '''

    # get count cards
    count_cards = get_count_cards()
    if 'error' in count_cards and count_cards['error'] is not None:
        return {
            'error': count_cards['error'],
            'message': count_cards['message'],
            'data': None
        }
    

    # get total questions per subject
    total_questions_per_subject = get_total_questions_per_subject()

    if 'error' in total_questions_per_subject and total_questions_per_subject['error'] is not None:
        return {
            'error': total_questions_per_subject['error'],
            'message': total_questions_per_subject['message'],
            'data': None
        }
        

    return {
        'error': None,
        'data': {
            'count_cards': count_cards['data'],
            'total_questions_per_subject': total_questions_per_subject['data']
        }
    }

def get_total_questions_per_subject():

    ## get all question papers

    all_question_papers = db.session.execute(
        db.select(QuestionPaper)
    ).scalars().all()

    ## for each question paper get the subject id and count the questions

    question_count_per_subject = {}
    for question_paper in all_question_papers:
        subject_id = question_paper.subject_id
        if subject_id not in question_count_per_subject:
            question_count_per_subject[subject_id] = 0
        question_count_per_subject[subject_id] += 1

    keys = list(question_count_per_subject.keys())
    values = list(question_count_per_subject.values())

    length_keys = len(keys)

    # generate random hex color for each subject
    colors = ['#' + ''.join([hex(i)[2:] for i in [random.randint(0, 255) for _ in range(3)]]) for _ in range(length_keys)]


    final_response = {
        'labels': keys,
        'datasets': [{
            'data': values,
            'backgroundColor': colors,
        }]
    }


    return {
        'error': None,
        'message': 'Total questions per subject fetched successfully',
        'data': final_response

    }


def get_count_cards():


    ## get count user with role evaluator
    ## get count of subjects
    ## get count of question papers

    try:
        user_count = db.session.execute(db.select(User)
                                        .where(User.role == 'EVALUATOR')).scalars().all()
        
        user_count = len(user_count)

        print(user_count)
        
    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while getting user count',
            'data': None
        }
    
    try:
        subject_count = db.session.execute(
            db.select(Subject)).scalars().all()
        
        subject_count = len(subject_count)

    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while getting subject count',
            'data': None
        }
    try:
        question_paper_count = db.session.execute(
            db.select(QuestionPaper)).scalars().all()
        
        question_paper_count = len(question_paper_count)


    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while getting question paper count',
            'data': None
        }
    return {
        'error': None,
        'message': 'Count cards fetched successfully',
        'data': {
            'user_count': user_count,
            'subject_count': subject_count,
            'question_paper_count': question_paper_count
        }
    }