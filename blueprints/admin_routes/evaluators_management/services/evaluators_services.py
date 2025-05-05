from db import db_methods as dbm
from db.models import User 

def new_evaluator(evaluator):
    """
    Create a new evaluator in the database.
    :param evaluator: The evaluator object to be created.
    :return: The created evaluator object.
    """
    random_string = ''.join(random.choices(
        string.ascii_letters + string.digits, k=8))
    
    result = dbm.insert_to_db(User(
        email=evaluator['email'],
        password='evaluator',
        role='EVALUATOR',
        active=True,
        created_date=dbm.get_current_time(),
        name=evaluator['name']
    ))