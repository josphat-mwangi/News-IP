import urllib.request,json
from .models import Source,Articles
import requests
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
    print(api_key)
    article_url = app.config['ARTICLE_API_BASE_URL']

    source_url = app.config['SOURCE_API_BASE_URL']




def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = source_url.format(api_key)

    get_process_response = requests.get(get_sources_url).json()

    
    

    sources_results = None
    

    if get_process_response['sources']:
        sources_results_list = get_process_response['sources']
        sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    '''
    Function that processes the news sources results and turns them into a list of objects
    Args:
            sources_list: A list of dictionaries that contain sources details
    Returns:
            sources_results: A list of sources objects
    '''
    sources_results = []

    for source_item in sources_list:
        id = source_item['id']
        name = source_item['name']
        description = source_item['description']
        url = source_item['url']
    
        category = source_item['category'] 
        if name:
            sources_object = Source(id, name, url, description, category)
            sources_results.append(sources_object)

    return sources_results


def get_articles():
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = article_url.format(api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())

        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object


def process_articles(articles_list):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    articles_object = []
    for article_item in articles_list:
        
        author = article_item['author']
        title = article_item['title']
        description = article_item['description']
        url = article_item['url']
        urlToImage = article_item['urlToImage']
        publishedAt = article_item['publishedAt']

        if urlToImage:
            articles_result = Articles(author, title, description, url, urlToImage, publishedAt)
            articles_object.append(articles_result)

    return articles_object


