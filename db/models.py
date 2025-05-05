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