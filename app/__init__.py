from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# HTTP error handling
@app.errorhandler(404)
def not_found(err):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (mod_auth)
from app.controllers.portfolio_controller import portfolio


# Register blueprint(s)
app.register_blueprint(portfolio)


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()