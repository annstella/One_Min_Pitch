import os

class Config:
    '''
    General configuration parent class
    '''
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    

    SQLALCHEMY_TRACK_MODIFICATIONS = False

# email configuration
    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    '''
    Pruduction configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
   
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://annstella:sterun@localhost/one_min_pitch'
   
    

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://annstella:sterun@localhost/one_min_pitch'
    SECRET_KEY = "annstella"

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}