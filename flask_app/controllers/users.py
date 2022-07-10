# Import app
from flask_app import app
# Import modules from flask
from flask import Flask, render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt

# Import models class
# Example: from flask_app.models.dojo import Dojo

# Create the routes

@app.route('/')
def index():
    """Homepage"""
    return render_template('index.html')


# TODO set routes to CREATE - INSERT into db in models
# TODO set routes to READ - SELECT from db in models
# TODO set routes to UPDATE - UPDATE from db in models
# TODO set routes to DELETE - DELETE from db in models
