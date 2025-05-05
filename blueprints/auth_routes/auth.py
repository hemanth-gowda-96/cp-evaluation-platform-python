
from flask import Blueprint, redirect, request, jsonify, render_template, session, flash

from blueprints.auth_routes.services import auth_services
from db.models import User
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.get('/login')
def login():
    ''' This function returns the login page '''

    if 'email' in session:
        flash("You are already logged in.", "info")
        return render_template('login/login.html', )

    flash("Please login to continue.", "info")

    return render_template('login/login.html', )

@bp.post('/login')
def login_post():
    ''' This function logs the user in '''

    email = request.form.get('email')
    password = request.form.get('password')

    response = auth_services.login(email, password)

    if response['error']:
        flash(response['error'], 'error')
        return render_template('login/login.html'), 400

    user_data: User = response['data']

    # set session
    session['email'] = user_data.email
    session['id'] = user_data.id
    session['name'] = user_data.name
    session['role'] = user_data.role
    session['active'] = user_data.active

    role = user_data.role

    if role == 'ADMIN':
        flash("Welcome Admin " + user_data.name, "success")
        return redirect('/admin/home'), 301

    if role == 'EVALUATOR':
        flash("Welcome Evaluator " + user_data.name, "success")
        return redirect('/evaluator/home'), 301

    flash("Invalid Credentials", "error")
    return render_template('login/login.html', ), 400


@bp.get('/logout')
def logout():
    ''' This function logs the user out '''

    session.clear()

    return redirect('/auth/login'), 301


@bp.get('/landing')
def landing():
    ''' This function returns the landing page '''

    if 'email' not in session:
        flash("Please Login First", "info")
        return redirect('/auth/login'), 301
    
    if session['role'] == 'ADMIN':
        return redirect('/admin/home'), 301
    
    if session['role'] == 'EVALUATOR':
        return redirect('/evaluator/home'), 301

    return render_template('login/landing.html', )