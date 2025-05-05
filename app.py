from flask import Flask, redirect, session
from flask_migrate import Migrate

from db.default_admin import create_default_admin, fetch_admin
from db.models import db

from config.config import config

# routes 
from blueprints.auth_routes import auth


app = Flask(__name__)

app.config.from_object(config['development'])


@app.route('/')
def redirect_to_login():
    ''' This function redirects the user to the login page '''

    print('Redirecting to login page')

    # # check if user is logged in
    # if 'email' in session:

    #     role = session['role']

    #     if role == 'ADMIN':
    #         return redirect('/admin/home')
    #     if role == 'STUDENT':
    #         return redirect('/users home')

    return redirect('/auth/login')

db.init_app(app)
migrate = Migrate(app, db)


# register blueprints
app.register_blueprint(auth.bp)

with app.app_context():
    db.create_all()
    
    create_default_admin(db)

    admin = fetch_admin()
    print(admin)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)