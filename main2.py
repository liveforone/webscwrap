"""
해당 코드는 html에서 id가 없는 경우 사용하며
오른쪽마우스 검사를 클릭후 오른쪽마우스 copy -> copy selector를 클릭하여 복사한 후 사용한다.
"""
import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/item/main.nhn?code=000660"
html = requests.get(url).text

soup = BeautifulSoup(html, "html5lib")
tags = soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")

for tag in tags:
     print(tag.text)