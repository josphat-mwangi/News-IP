from flask import render_template
from app import app
from .request import get_source, get_article, search_source

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
    sport = get_source('sport')
    politics = get_source('politics')
    business = get_source('business')
    searched_source = search_source(source_name_format)

    return render_template('source.html' sport=sport, politics=politics, business=business)


@app.route('/article')
def source(article_id):
    '''
    View article page function that returns article details page and its data
    '''
    article = get_article()
    return render_template('article.html' article=article)
