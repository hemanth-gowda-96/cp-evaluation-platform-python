''' all shared common db methods '''

from db.models import db

# create db method


def insert_to_db(data):
    ''' insert data to db '''

    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        if 'UNIQUE constraint failed' in str(e):
            return {
                'error': str(e),
                'message': 'Data already exists in db',
                'data': None
            }
        return {
            'error': str(e),
            'message': 'Error inserting data to db',
            'data': None
        }

    return {
        'status': 'success',
        'message': 'inserted data to db',
        'data': data
    }
