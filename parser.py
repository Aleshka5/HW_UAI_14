import requests
from bs4 import BeautifulSoup
import time
filters = ['python','machine learning','ml','машинное обучение','машинное обучение','data science','ds','глубокое обчуение','нейронные сети']
theme_articles = []
for i in range(1,50):
    time.sleep(5)
    url = f'https://habr.com/ru/flows/develop/page{i}/'
    response = requests.get(url)
    print(i, response.status_code)
    #print(response.text)
    soup = BeautifulSoup(response.text,'html.parser')
    for ref in soup.find_all('a'):
        #print(ref['class'])
        #print(type(ref))
        try:
            if ref['class'][0] == 'tm-article-snippet__title-link':
                for filter in filters:
                    if filter in str(ref.string).lower():
                        theme_articles.append(str(ref.string).lower())
                        break
        except:
            pass
print(theme_articles)