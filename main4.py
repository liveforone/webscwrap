import requests
import datetime

jsObj = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
bitcoin = jsObj.json()

time = bitcoin['timestamp']
#formtimestamp로 편리한 datetime으로 변환한다.
date = datetime.datetime.fromtimestamp(time/1000)
print(date)