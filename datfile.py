import requests
import json

news_api_key = '0b19c9bde21541859e8176ed2060de79'
telegram_key = '5247888467:AAH2hPIdtmH26P3mhdCKkpSua9Pt44mYoY0'


def get_news_api_key():
	return news_api_key


def get_telegram_key():
	return telegram_key

headers = {'X-Api-Key': news_api_key}


def get_news_from_keyword(keyword):
    news_url = 'https://newsapi.org/v2/everything?language=en&q=' + keyword

    response = requests.get(news_url, headers=headers).text 
    response = json.loads(response)['articles']
    return_list = []
    for r in response:
        source = r['source']['name']
        author = r['author']
        title = r['title']
        url = r['url']
        return_list.append(
            '\n\nAgency: ' + str(source) + '\nAuthor :' + str(author) + '\nTitle: ' + title + '\n\nread here: ' + str(
                url))
    if len(return_list) > 5:
        return return_list[:5]

    return return_list


def get_news_from_topic(topic):
    return get_news_from_keyword(topic)
