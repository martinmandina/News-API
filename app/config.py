class Config:
    NEWS_API_BASE_URL = "https://newsapi.org/v2/top-headlines{}?apiKey={}"

class ProdConfig(Config):
    pass

class DevConfig(Config):
    pass

    DEBUG = True
