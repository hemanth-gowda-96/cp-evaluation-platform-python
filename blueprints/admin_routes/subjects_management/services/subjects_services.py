
from db import db_methods as dbm
from db.models import Subject
from db.models import db


def new_subject(subject: dict) -> dict:
    """
    Create a new subject.
    """
    result = dbm.insert_to_db(Subject(
        code=subject['code'],
        name=subject['name'],
        description=subject['description'],
        department=subject['department'],
        semester=subject['semester'],
        active=True,
    ))

    if 'error' in result and result['error'] is not None:
        return {
            'error': result['error'],
            'data': None,
            'message': result['message']
        }

    return {
        'error': None,
        'message': 'Subject created successfully',
        'data': result['data']
    }


def search_subjects_service() -> dict:
    """
    Search for subjects.
    """
    try:
        subjects = db.session.execute(
            db.select(Subject).order_by(Subject.code)).scalars().all()
    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while searching subjects',
            'data': None
        }

    return {
        'error': None,
        'message': 'search successful',
        'data': subjects
    }
