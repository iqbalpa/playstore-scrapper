from google_play_scraper import app

result = app(
    'com.sayurbox',
    lang='id', # defaults to 'en'
    country='id' # defaults to 'us'
)

print(result)