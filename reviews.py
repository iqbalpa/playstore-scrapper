from google_play_scraper import Sort, reviews
import utils

list_app = ['segari', 'astro', 'sayurbox', 'titipku', 'my super indo', 'hypermart', 'happyfresh']

result, continuation_token = reviews(
    'com.sayurbox',
    lang='id', # defaults to 'en'
    country='id', # defaults to 'us'
    sort=Sort.NEWEST, # defaults to Sort.NEWEST
    count=3, # defaults to 100
    filter_score_with=5 # defaults to None(means all score)
)

# If you pass `continuation_token` as an argument to the reviews function at this point,
# it will crawl the items after 3 review items.

result, _ = reviews(
    'com.sayurbox',
    continuation_token=continuation_token # defaults to None(load from the beginning)
)

print(result)