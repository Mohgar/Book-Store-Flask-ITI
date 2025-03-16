import os

class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or "default_secret_key"
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    SECRET_KEY = "local_development_key"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

class ProductionConfig(BaseConfig):
    DEBUG = False

Config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}