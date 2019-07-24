from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    def signup_post():
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/login', methods=['POST'])
def login_post():
    #login code here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=email).first()

    if not user: 
        flash('We dont have that email. Try again.')
        return redirect(url_for('auth.login'))
    elif not check_password_hash(user.password, password):
        flash('Wrong password {}'.format(email))
        return redirect(url_for(auth.login))
    return redirect(url_for('main.profile'))




