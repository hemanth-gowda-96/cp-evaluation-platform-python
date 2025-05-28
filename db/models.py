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

class QuestionPaper(db.Model):
    __tablename__ = 'question_papers'

    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.String(255), unique=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    subject_id = db.Column(db.String(255), nullable=False)  # Should reference Subject table
    exam_date = db.Column(db.Date, nullable=False)
    semester = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)  # Name of the file
    file_data = db.Column(db.LargeBinary, nullable=True)  # Stores the actual file as BLOB
    upload_date = db.Column(db.DateTime, server_default=db.func.now())
    duration_minutes = db.Column(db.String(255))
    max_marks = db.Column(db.String(255))
    status = db.Column(db.String(255), nullable=False, default='PENDING')  # PENDING, APPROVED, REJECTED