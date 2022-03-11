import urllib.request,json



#getting api key
api_key =None

def configure_request(app):
    global api_key

    api_key =app.config['RANDOM_QUOTE_API_KEY']