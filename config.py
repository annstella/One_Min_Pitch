import os

class Config:


 class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://annstella:sterun@localhost/watchlist'


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}