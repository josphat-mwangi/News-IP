from flask import render_template, request, redirect,url_for
from . import main
from ..request import get_sources, get_articles
# from newsapi import NewsApiClient
# # views
from ..models import Source


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data 

    '''
    title = 'Home - Welcome to The best News and Article website Online'

    return render_template('index.html', title=title)


@main.route('/source')
def source():
    '''
    View source page function that returns source details page and its data
    '''
    sources = get_sources()
    # print(sources)
    # sports_sources = get_sources()
    # technology_sources = get_sources()
    # entertainment_sources = get_sources()
    
    return render_template('source.html',  sources=sources)

        
    


@main.route('/article')
def article():
    '''
    View article page function that returns article details page and its data
    '''
    article = get_articles()
    return render_template('article.html', article=article)
    
