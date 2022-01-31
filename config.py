class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michel:mishy@localhost/sms_data'
    SECRET_KEY = "mishatieno23"


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michel:mishy@localhost/sms_data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

