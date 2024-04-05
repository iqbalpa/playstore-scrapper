from google_play_scraper import app

list_app = ['segari', 'astro', 'sayurbox', 'titipku', 'my super indo', 'hypermart', 'happyfresh']

result = app(
    'com.sayurbox',
    lang='id', # defaults to 'en'
    country='id' # defaults to 'us'
)

print(result)