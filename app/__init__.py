from flask import Flask
from flask_bootstrap import Bootstrap
from .config import DevConfig

# Initializing application

app = Flask(__name__)

# Setting up confinguration 
app.config.from_object(DevConfig)

from app import views