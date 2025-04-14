from flask import Blueprint, render_template

# Create a Blueprint for the main app routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
