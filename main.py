from bs4 import BeautifulSoup
import requests
import json

headers_browser = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
link = 'https://www.washingtonpost.com/latest-headlines/'
news_list = []

response = requests.get(link, headers=headers_browser).text
soup = BeautifulSoup(response, 'lxml')
news_card = soup.findAll(class_='left wrap-text art-size--sm')
for items in news_card:
    news_header = items.find(class_='headline relative gray-darkest pb-xs').text
    news_descr = items.find(class_='pb-xs font-size-blurb lh-fronts-tiny font-light gray-dark').text
    news_link = items.find(class_='pb-xs font-size-blurb lh-fronts-tiny font-light gray-dark').find('a')['href']

    news_item = {
        'header': news_header,
        'description': news_descr,
        'link': news_link
    }
    news_list.append(news_item)

with open('latest_news.json', 'w', encoding='utf-8') as json_file:
    json.dump(news_list, json_file, ensure_ascii=False, indent=4)
