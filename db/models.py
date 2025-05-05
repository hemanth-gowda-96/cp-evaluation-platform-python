from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    ''' This class represents the user model '''

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(80), nullable=False)
    active = db.Column(db.Boolean, nullable=False, default=True)
    created_date = db.Column(db.DateTime, nullable=True,
                             server_default=db.func.now())
    name = db.Column(db.String(80), nullable=False)
    department = db.Column(db.String(80), nullable=True)
    designation = db.Column(db.String(80), nullable=True)
    phone_number = db.Column(db.String(80), nullable=True)


class Subject(db.Model):
    ''' This class represents the subject model '''

    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(db.DateTime, nullable=True,
                             server_default=db.func.now())
    active = db.Column(db.Boolean, nullable=False, default=True)
    code = db.Column(db.String(80), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=True)
    department = db.Column(db.String(80), nullable=True)
    semester = db.Column(db.String(80), nullable=True)
