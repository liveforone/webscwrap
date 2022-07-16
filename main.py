"""
해당 코드는 html에서 id가 있는 태그를 스크래핑하는 경우 사용이 가능하다.
"""
import requests
from bs4 import BeautifulSoup

def get_per(code):  #per지수
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_per")  #id = _per임
    tag = tags[0]  #첫번째 em 태그를 가져옴
    return float(tag.text)

def get_dividend(code):  #배당수익률
    url = "http://finance.naver.com/item/main.nhn?code=" + code
    html = requests.get(url).text

    soup = BeautifulSoup(html, "html5lib")
    tags = soup.select("#_dvr")
    tag = tags[0]
    return float(tag.text)

print(get_per("000660"))
print(get_dividend("000660"))