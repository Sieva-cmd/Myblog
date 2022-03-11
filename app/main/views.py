
from flask import render_template
from . import main

#views
@main.route('/')
def index():

    title = 'My blog'

    return render_template('index.html',title=title)