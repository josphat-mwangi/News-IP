from flask import render_template
from app import app

# views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data 

    '''
    title = 'Home - Welcome to The best News and Article website Online'
    return render_template('index.html', title=title)
