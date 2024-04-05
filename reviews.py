from google_play_scraper import Sort, reviews
import utils

list_app = ['segari', 'astro', 'sayurbox', 'titipku', 'my super indo', 'hypermart', 'happyfresh']
list_app = {
    'segari': 'id.segari.customer', 
    'astro': 'com.astro.shop',
    'sayurbox': 'com.sayurbox',
    'hypermart': 'com.hypermart.mobile',
    'happyfresh': 'com.happyfresh.android'
}

for app in list_app:
    result, continuation_token = reviews(
        list_app[app],
        lang='id', # defaults to 'en'
        country='id', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=100, # defaults to 100
        filter_score_with=None # defaults to None(means all score)
    )
    result, _ = reviews(
        list_app[app],
        continuation_token=continuation_token # defaults to None(load from the beginning)
    )

    utils.save_data(result, f"data/{app}.json")