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


@app.route('/source')
def source(source_id):
    '''
    View source page function that returns source details page and its data
    '''
    return render_template('source.html')


@app.route('/article')
def source(source_id):
    '''
    View article page function that returns article details page and its data
    '''
    return render_template('article.html')
