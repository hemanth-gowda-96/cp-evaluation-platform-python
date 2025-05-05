''' auth services '''


from db.models import User

from db import db_methods as dbm


def login(email, password):
    ''' This function logs the user in '''

    # get users

    response = get_user(email)

    if response['error']:
        return response

    # match password

    user_data: User = response['data']

    if user_data.password != password:
        return {
            'error': 'Invalid Credentials',
            'data': None
        }

    # if user is not active

    if not user_data.active:
        return {
            'error': 'Invalid Credentials',
            'data': None
        }

    return {
        'error': None,
        'data': user_data
    }


def get_user(email):
    ''' This function gets the user '''

    user = User.query.filter_by(email=email).first()

    if user is None:
        return {
            'error': 'Invalid Credentials',
            'data': None
        }

    return {
        'error': None,
        'data': user
    }


def validate_registration(data: dict):
    ''' This function validates the registration data '''

    full_name = data.get('full_name')
    email = data.get('email')
    student_id = data.get('student_id')
    student_department = data.get('department')
    semester = data.get('semester')


    if not full_name or not email or not student_id or not student_department or not semester:
        return {
            'error': 'All fields are required',
            'data': None
        }

    return {
        'error': None,
        'data': data
    }


def register_new_student(data: dict):
    ''' service to register new student '''

    full_name = data.get('full_name')
    email = data.get('email')
    student_id = data.get('student_id')
    student_department = data.get('department')
    semester = data.get('Semester')

    user = User(
        name=full_name,
        email=email,
        password="student",
        role='STUDENT',
        active=True,
        student_id=student_id,
        student_department=student_department,
        student_semister=semester
    )

    result = dbm.insert_to_db(user)


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
