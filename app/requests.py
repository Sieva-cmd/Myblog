import urllib.request,json
from .models import Quote



#getting api key
# api_key =None

# def configure_request(app):
#     # global api_key

#     # api_key =app.config['RANDOM_QUOTE_API_KEY']

def get_quote():
    qoute_api_url ='http://quotes.stormconsultancy.co.uk/random.json'
    with urllib.request.urlopen( qoute_api_url ) as url:
        get_quotes_data =url.read()
        quote_response =json.loads(get_quotes_data)

        quotes_object =None
        if quote_response:
            author =quote_response.get('author')
            quote =quote_response.get('quote')

            quotes_object =Quote(author,quote)
        print(quotes_object)    
        return(quotes_object)    
