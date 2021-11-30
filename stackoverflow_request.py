import requests
import datetime


def get_questions_with_py_tags():
    today = datetime.date.today()
    yesterday = datetime.date(today.year, today.month, today.day - 1)
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': f'{yesterday}', 'todate': f'{today}', 'order': 'desc', 'sort': 'activity',
              'site': 'stackoverflow', 'tagged': 'python', 'filter': 'default'}
    response = requests.get(url=url, params=params)
    for item in response.json()['items']:
        if len(item["title"]) <= 50:
            print(f'"{item["title"]}" Link [{item["link"]}]')
        else:
            print(f'"{item["title"][:50]}..." Link [{item["link"]}]')
