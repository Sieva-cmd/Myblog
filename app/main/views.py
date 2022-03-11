
from flask import render_template
from . import main
from flask_login import login_required

#views
@main.route('/')
@login_required
def index():

    title = 'My blog'

    return render_template('index.html',title=title)