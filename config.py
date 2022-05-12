import os 

class Config:
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard stuff to crack'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
<<<<<<< HEAD
    MAIL_PORT = 58
=======
    MAIL_PORT = 587
>>>>>>> 2583607409e4dc74893d4796afb42b43198177a2
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    UPLOADED_PHOTOS_DEST ='app/static/photos'

class DevConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:morces@localhost/pitches'

DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:morces@localhost/pitches_test'

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "")
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI.replace('postgres://','postgresql://',1)

    
config_options = {
    'development':DevConfig,
    'production' :ProdConfig,
    'test' :TestConfig
}