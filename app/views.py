from flask import render_template,request,redirect,url_for
from app import app
from .request import get_sources




@app.route('/')
def index():
    '''
    This is the view root page function that returns the index page and its data
    '''
    business_news = get_sources('business')
    entertainment_news = get_sources('entertainment')
    technology_news = get_sources('technology')
    health_news = get_sources('health')

    title = 'News - Top News And Stories For You'
    return render_template('index.html',title = title,business_news = business_news,entertainment_news = entertainment_news,technology_news = technology_news, health_news =  health_news)
    
@app.route('/news/<int:news_id>')
def news(news_id):

    return render_template('news.html',id = news_id)
    