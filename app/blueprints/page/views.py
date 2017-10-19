from flask import Blueprint, render_template

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    return "Hello from flask!"


@page.route('/home')
def terms():
    return render_template('page/index.html')