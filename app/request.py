import urllib.request,json
from .models import Source,Articles

# Getting api key
api_key = None

# Getting base url
source_url = None
article_url = None


def configure_request(app):
    '''
    Create a function configure_request

    '''
    global api_key, article_url, source_url
    api_key = app.config['NEWS_API_KEY']
    article_url = app.config['ARTICLE_API_BASE_URL']
    source_url = app.config['SOURCE_API_BASE_URL']


def get_source(Category):
    '''
    function that gets the json response to our url request

    '''
    get_source = source_url.format(Category, api_key)
    with urllib.request.urlopen(get_source) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['results']:
            source_results_list = get_source_response['results']

            source_results = process_results(source_results_list)

    return source_results



def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        Category = source_item.get('Category')

        if Category:
            movie_object = Movie(id, name, Category)
            source_results.append(source_object)

    return source_results


def get_article(source):
    '''
    function that process the article results and transform them to a 
    '''
    get_article_url = article_url.format(api_key)

    with urllib.request.urlopen(get_article_url)as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_article_response['articles']:
            article_results_list = get_article_response['article']
            article_results = process_results(article_results_list)

    return article_results


def process_results(article_list):
    '''
    Function  that processes the article result and transform them to a list of Objects

    Args:
        article_list: A list of dictionaries that contain article details

    Returns :
        article_results: A list of article objects
    '''
    article_results = []
    for article_item in article_list:
        author = article_item.get('author')
        title = article_item.get('original_title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishdate = movie_item.get('publishedAt')

        if urlToImage:
            article_object = Articles(
                author, title, description, url, urlToImage, publishe)
            article_results.append(article_object)

    return article_results


def search_source(source_name):
    search_sourec_url = 'http: // newsapi.org/v2/everything?q{}apiKey = {}'.format(
        api_key, source_name)
    with urllib.request.urlopen(search_source_url) as url:
        search_source_data = url.read()
        search_source_response = json.loads(search_source_data)

        search_source_results = None

        if search_source_response['results']:
            search_source_list = search_source_response['results']
            search_source_results = process_results(search_source_list)

    return search_source_results
