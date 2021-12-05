
# import beautiful soup
from bs4 import BeautifulSoup
import requests
import datetime
from translator import englishToFrench

url = 'https://www.indiatoday.in/world'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

class NewsItem:
    def __init__(self, title_en, desc_en, image_url):
        self.title_en = title_en
        self.desc_en = desc_en
        self.image_url = image_url
        self.title_fr = englishToFrench(title_en)
        self.desc_fr = englishToFrench(desc_en)
        self.timestamp = datetime.datetime.now()

def getNewsList():
    news = []
    for item in soup.find_all(class_ = 'catagory-listing'):
        image_url = item.find('img')['src']
        title_en = item.find('a').text
        desc_en = item.find('p').text
        news.append(NewsItem(title_en, desc_en, image_url))
    return news