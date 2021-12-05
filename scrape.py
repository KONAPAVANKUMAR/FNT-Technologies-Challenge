
# import beautiful soup
from bs4 import BeautifulSoup
import requests

url = 'https://www.indiatoday.in/world'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

class NewsItem:
    def __init__(self, title, description, imageUrl):
        self.title = title
        self.description = description
        self.imageUrl = imageUrl

def getNewsList():
    news = []
    for item in soup.find_all(class_ = 'catagory-listing'):
        imageUrl = item.find('img')['src']
        title = item.find('a').text
        description = item.find('p').text
        news.append(NewsItem(title, description, imageUrl))
    return news