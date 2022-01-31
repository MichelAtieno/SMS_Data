class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michel:mishy@localhost/sms_data'
    SECRET_KEY = "mishatieno23"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    if ENV == 'dev':
        SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://michel:mishy@localhost/sms_data'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    else:
        SQLALCHEMY_DATABASE_URI = 'postgres://issqhfagymjxlu:bd5008e19565cd3584f8235a963362e41174d600ce1efa177094d20179985ac2@ec2-3-216-113-109.compute-1.amazonaws.com:5432/d49etab5oknvkr'


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

