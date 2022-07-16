import requests

jsObj = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin = jsObj.json()
print(bitcoin)
print(bitcoin['last']) #종가(최종체결가)가져옴
print(bitcoin['bid']) #최우선 매수호가 (매수 수문 중 가장 높은 가격)
print(bitcoin['ask']) #최우선 매도 호가 (매도 주문 중 가장 낮은 가격)
print(bitcoin['low']) #최근 24시간 저가
print(bitcoin['high']) #최근 24시간 고가
print(bitcoin['volume']) #거래량
print(bitcoin['timestamp']) #최종 체결 시각