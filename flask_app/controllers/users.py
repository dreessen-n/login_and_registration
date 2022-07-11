# Import app
from flask_app import app
# Import modules from flask
from flask import Flask, render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt

# Import models class
from flask_app.models import user

# Create the routes

@app.route('/')
def index():
    """Homepage"""
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def regitster():
    """Register new user"""
    # Call staticmethod to validate form
    if not user.User.validate_user(request.form):
        # Redirect back to registration page
        return redirect('/')
    # Create data dict based on request form
    # the keys must match exactly to the var in the query set
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password']
    }
    # Pass the data dict to create_user method in class
    user.User.create_user(data)
    # Redirect to the welcome page
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    """Welcome page"""
    return render_template('Welcome.html')

# TODO set routes to CREATE - INSERT into db in models
# TODO set routes to READ - SELECT from db in models
# TODO set routes to UPDATE - UPDATE from db in models
# TODO set routes to DELETE - DELETE from db in models
