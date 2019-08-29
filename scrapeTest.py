import urllib3
from bs4 import BeautifulSoup

url = "http://www.nikkei.com/"

http = urllib3.PoolManager()

html = http.request('GET', url)

soup = BeautifulSoup(html.data, "html.parser")

titleTag = soup.title

title = titleTag.string

print(titleTag)

print(title)
