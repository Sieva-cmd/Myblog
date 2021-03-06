import os

class Config:
    RANDOM_QUOTE_API_KEY =os.environ.get('RANDOM_QUOTE_API_KEY')
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:sieva@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    # MAIL_SERVER = 'smtp.googlemail.com'
    # MAIL_PORT = 587
    # MAIL_USE_TLS = True
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    

class ProdConfig(Config):
    pass


class DevConfig(Config):

    Debug =True


config_options ={
    'development':DevConfig,
    'production':ProdConfig

}    