
# import beautiful soup
from bs4 import BeautifulSoup
import requests
import datetime
from translator import englishToFrench

url = 'https://www.indiatoday.in/world?page=1'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

class NewsItem:
    def __init__(self, title_en, desc_en, image_url):
        self.title_en = title_en
        self.desc_en = desc_en
        self.image_url = image_url
        self.title_fr = None
        self.desc_fr = None
        self.timestamp = datetime.datetime.now()

def getNewsList():
    news = []
    toTranslate = []
    for item in soup.find_all(class_ = 'catagory-listing'):
        image_url = item.find('img')['src']
        title_en = item.find('a').text
        desc_en = item.find('p').text
        toTranslate.append(title_en)
        toTranslate.append(desc_en)
        news.append(NewsItem(title_en, desc_en, image_url))
    toTranslate = "$".join(toTranslate)
    toTranslate = englishToFrench(toTranslate).split("$")
    print(len(toTranslate))
    for i in range(len(news)-1):
        news[i].title_fr = toTranslate[i*2]
        news[i].desc_fr = toTranslate[i*2+1]
    return news