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

def scrap_reviews(app_id, app_name):
    result, continuation_token = reviews(
        app_id,
        lang='id', # defaults to 'en'
        country='id', # defaults to 'us'
        sort=Sort.NEWEST, # defaults to Sort.NEWEST
        count=100, # defaults to 100
        filter_score_with=None # defaults to None(means all score)
    )
    result, _ = reviews(
        app_id,
        continuation_token=continuation_token # defaults to None(load from the beginning)
    )
    return app_name, result

def main():
    for app_name, app_id in list_app.items():
        print(f'scraping {app_name}...')
        app_name, result = scrap_reviews(app_id, app_name)
        utils.save_data(result, f'data/{app_name}.json')
        print(f'{app_name} done...')


if __name__ == '__main__':
    main()