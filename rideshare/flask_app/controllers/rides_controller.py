from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user_model import Users
from flask_app.models.ride_model import Rides
from flask_app.models.message_model import Messages

@app.route('/rides/dashboard')
def posts():
    if 'user_id' not in session:
        return redirect('/')
    user = {
        "id": session['user_id']
    }
    return render_template('dashboard.html', user = Users.get_by_id(user), requests =Rides.get_all_ride_requests(), booked_rides=Rides.get_all_ride_booked())

@app.route('/rides/new')
def request_new_ride():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('new.html')

@app.route('/ride/create', methods=["POST"])
def createing_new_ride():
    if not Rides.validate_create_ride(request.form):
        session['destination'] = request.form['destination']
        session['pick_up'] = request.form['pick_up']
        session['details'] =request.form['details']
        return redirect('/ride/new')
    data ={
        'destination': request.form['destination'],
        'pick_up': request.form['pick_up'],
        'date': request.form['date'],
        'details': request.form['details'],
        'rider_id': session['user_id']
    }
    Rides.create_ride(data)
    return redirect('/rides/dashboard')

@app.route('/ride/delete/<int:id>')
def remove_ride(id):
    data ={
        "id": id
    }
    print("well we got his far")
    Rides.delete_ride(data)
    return redirect('/rides/dashboard')

@app.route('/ride/accept/<int:id>')
def add_driver(id):
    data ={
        "id": id,
        "driver_id": session['user_id']
    }
    Rides.driver_accpet(data)
    return redirect('/rides/dashboard')

@app.route('/ride/details/<int:id>')
def ride_details(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    return render_template('details.html', ride=Rides.get_one_ride(data), messages=Messages.get_all_messages(data))

@app.route('/message/add', methods=["POST"])
def add_message():
    data = {
        'content': request.form['content'],
        'ride_id': request.form['ride_id'],
        'user_id': session['user_id']
    }
    Messages.create_message(data)
    ride = request.form['ride_id']
    return redirect(f'/ride/details/{ride}')

@app.route('/ride/cancel/<int:id>')
def cancel_driving(id):
    data ={
        "id": id
    }
    Rides.cancel_driver(data)
    return redirect('/rides/dashboard')

@app.route('/ride/edit/<int:id>')
def edit_view(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "id": id
    }
    return render_template('edit.html', ride=Rides.get_one_ride(data))

@app.route('/ride/update/<int:id>', methods=["POST"])
def change_ride(id):
    if not Rides.validate_edit_ride(request.form):
        return redirect(f'/ride/edit/{id}')
    data ={
        'id': id,
        'pick_up': request.form['pick_up'],
        'details': request.form['details']
    }
    Rides.update_ride(data)
    return redirect(f'/ride/details/{id}')