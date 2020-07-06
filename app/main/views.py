from flask import render_template, request, redirect,url_for
from . import main
from ..request import get_source, get_article, search_source

# views


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data 

    '''
    title = 'Home - Welcome to The best News and Article website Online'

    return render_template('index.html', title=title)


@main.route('/source')
def source(source_id):
    '''
    View source page function that returns source details page and its data
    '''
    sport = get_source('sport')
    politics = get_source('politics')
    business = get_source('business')
    searched_source = search_source(source_name_format)

    search_source = request.args.get('source_query')

    if search_source:
        return redirect(url_for('search', source_name=search_source))
    else:
        return render_template('source.html', sport = sport, politics = politics, business = business)


# @main.route('/article')
# def source(article_id):
#     '''
#     View article page function that returns article details page and its data
#     '''
#     article = get_article()
#     return render_template('article.html', article=article)
