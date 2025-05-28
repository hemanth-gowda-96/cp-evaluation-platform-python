'''  '''

import random
import string
from db import db_methods as dbm
from db.models import db
from db.models import User


def new_evaluator(email, name, department, designation, phone_number):
    """
    Create a new evaluator in the database.
    :param evaluator: The evaluator object to be created.
    :return: The created evaluator object.
    """
    random_string = ''.join(random.choices(
        string.ascii_letters + string.digits, k=8))

    result = dbm.insert_to_db(User(
        email=email,
        password='evaluator',
        role='EVALUATOR',
        active=True,
        name=name,
        department=department,
        designation=designation,
        phone_number=phone_number,
    ))

    if 'error' in result:
        return {
            'error': result['error'],
            'data': None,
            'message': result['message']
        }

    return {
        'error': None,
        'message': 'registration successful',
        'data': {}
    }


def search_evaluvators_service():
    ''' search student service '''

    try:
        users = db.session.execute(
            db.select(User).filter_by(role='EVALUATOR').order_by(User.email)).scalars().all()
    except Exception as e:
        return {
            'error': str(e),
            'message': 'An error occurred while searching evaluators',
            'data': None
        }

    return {
        'error': None,
        'message': 'search successful',
        'data': users
    }
