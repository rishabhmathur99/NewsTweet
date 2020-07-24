import requests

API_TOKEN = '458c4e4848a687a482dd8924c5a92fb0'

def getArticles(keywords):
    keyword_string = ' | '.join(keywords)
    url = f'https://gnews.io/api/v3/search?q={keyword_string}&token={API_TOKEN}'
    print(url)
    resp = requests.get(url)

    if resp.status_code != 200:
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))

    for article in resp.json()['articles']:
        print(article['title'])

    if resp.json()['articles'] is None:
        return []
    return resp.json()['articles']