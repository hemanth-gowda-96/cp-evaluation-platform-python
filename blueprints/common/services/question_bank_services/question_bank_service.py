

from db.models import QuestionPaper
from db import db_methods as dbm

from db.models import db


def create_new_question_bank_service(data: dict):
    ''' This function creates a new question bank '''
    

    question_bank = QuestionPaper(
        paper_id=data['code'],
        title=data['title'],
        description=data['description'],
        subject_id=data['subject_code'],
        semester=data['semester'],
        duration_minutes=data['duration'],
        max_marks=data['max_marks'],
        exam_date=data['exam_date'],
        file_name=data['file_name'],
        file_data=data['file_data'],
        status='PENDING'
    )

    result = dbm.insert_to_db(question_bank)
    if 'error' in result:

        print(result['error'])

        return {
            'error': result['error'],
            'data': None,
            'message': result['message']
        }
    

    return {
        'error': None,
        'message': 'Question bank created successfully',
        'data': question_bank
    }

def search_question_bank_service():
    ''' This function returns the question bank '''
    
    try:
        question_banks = db.session.execute(
            db.select(QuestionPaper).order_by(QuestionPaper.paper_id)).scalars().all()
    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while searching question banks',
            'data': None
        }

    return {
        'error': None,
        'message': 'search successful',
        'data': question_banks
    }

    
    
def get_question_bank_service(paper_id: str):
    ''' This function returns the question bank '''
    
    try:
        question_bank = db.session.execute(
            db.select(QuestionPaper).where(QuestionPaper.paper_id == paper_id)).scalars().one()
    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while searching question banks',
            'data': None
        }

    return {
        'error': None,
        'message': 'search successful',
        'data': question_bank
    }

def update_status_question_bank_service(paper_id: str, status: str):
    ''' This function updates the status of the question bank '''
    
    try:
        question_bank = db.session.execute(
            db.select(QuestionPaper).where(QuestionPaper.paper_id == paper_id)).scalars().one()
    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while searching question banks',
            'data': None
        }

    question_bank.status = status

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return {
            'error': str(e),
            'message': 'An error occurred while updating question bank',
            'data': None
        }

    return {
        'error': None,
        'message': 'Question bank updated successfully',
        'data': question_bank
    }