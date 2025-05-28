''' on app start check if admin available if not create on in db '''

from db.models import User


def create_default_admin(db):
    ''' This function creates the default admin user '''

    if User.query.filter_by(
        email='admin@mail.com'
    ).first() is None:

        admin = User(
            name='admin',
            password='admin',
            email="admin@mail.com",
            role='ADMIN',
            active=True

            #
        )

        db.session.add(admin)
        db.session.commit()

        print('Admin created successfully')
    else:

        print('Admin already exists')


def fetch_admin():
    ''' This function fetches the default admin user '''

    return User.query.filter_by(
        email='admin@mail.com'
    ).first()
