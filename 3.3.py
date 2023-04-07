from bs4 import BeautifulSoup as bs
import requests

url = 'https://search.naver.com/search.naver?where=news&query=삼쩜삼&sm=tab_opt&sort=1'


response = requests.get(url)
html_text=response.text

soup = bs(html_text, 'html.parser')

titles = soup.select('a.news_tit')

for i in titles:
    title = i.get_text()
    url = i.get("href")
    print(title, url)
