# Import app
from flask_app import app
# Import modules from flask
from flask import Flask, render_template, request, redirect, session, url_for
from flask_app import bcrypt

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
    if not user.User.validate_registration(request.form):
        # Redirect back to registration page
        return redirect('/')
    # Create data dict based on request form
    # the keys must match exactly to the var in the query set
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    # Pass the data dict to create_user method in class
    # After insert the db returns the user_id; save it
    user_id = user.User.create_user(data)
    # Check we have a user_id; is yes save into session
    if user_id:
        session['id'] = user_id
    # Redirect to the welcome page
    return redirect('/welcome')

@app.route('/welcome')
def welcome():
    """Welcome page"""
    # Create data set to query user based on id to get name to display
    data = {
        'id': session['id']
    }
    # Pass the data dict to create_user method in class
    one_user = user.User.get_user_by_id(data)
    print(one_user.first_name, one_user.last_name)
    return render_template('welcome.html', one_user=one_user)

@app.route('/logout')
def logout():
    """Logged the user out of seesion and redirect to login"""
    session.clear()
    return redirect('/')
