import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michel:mishy@localhost/sms_data:5432/postgres'
    SECRET_KEY = "mishatieno23"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') or 'postgresql+psycopg2://michel:mishy@localhost/sms_data:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michel:mishy@localhost/sms_data:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

