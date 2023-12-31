from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.user_model import Users
from flask import render_template, redirect, request, session, flash


bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/user/create', methods=['POST'])
def create():
    if not Users.validate_user(request.form):
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        return redirect('/')
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    if Users.get_by_email(data):
        flash('That email already exists, please log in or use another email','register')
        return redirect('/')
    new_id = Users.save(data)
    session['user_id'] = new_id
    return redirect('/rides/dashboard')

@app.route('/user/login',methods=['POST'])
def login():
    user = Users.get_by_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/rides/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')