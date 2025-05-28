''' config file read from .env file '''

import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, os.pardir))


class Config:
    ''' Parent configuration class '''

    SECRET_KEY = os.getenv('SECRET_KEY')


class DevelopmentConfig:
    ''' Development configuration class '''

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(PROJECT_ROOT, "datastore", "database.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


class ProductionConfig:
    ''' Production configuration class '''

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + \
        os.path.join(BASE_DIR, "datastore", "database.db")
    PROJECT_ROOT = False
    SECRET_KEY = os.getenv('SECRET_KEY')


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
