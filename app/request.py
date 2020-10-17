from app import app
import urllib.request,json
from .models import movie

News = news.News

api_key = app.config['NEWS_API_KEY']

base_url = app.config[' NEWS_API_BASE_URL']

def get_news(top_headlines):
    get_news_url = base_url.format(top_headlines,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None

        if get_news_response['results']
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results

