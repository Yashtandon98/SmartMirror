from bs4 import BeautifulSoup as soup
import requests


def getnews():
    ndata = []
    try:
        url = 'https://news.google.com/news/rss'
        c = requests.get(url)
        page = c.content
        sp = soup(page, 'xml')
        newslist = sp.findAll('item')
        for news in newslist[:5]:
            ndata.append(news.title.text)
    except Exception as e:
        print(e)
        ndata = None

    return ndata
