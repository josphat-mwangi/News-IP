# from newsapi import NewsApiClient
from flask import Blueprint
main = Blueprint('main', __name__)


# newsapi = NewsApiClient(api_key='fd3949e9fc8d439f8d810573dc948437')


from . import views, error
