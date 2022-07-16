<h2>main.py<h2>
<pre>
파이썬에서 웹 페이지 다운로드는 requests 모듈을 사용하고 
웹 페이지에서 원하는 데이터를 가져가는 파싱(parsing)은 BeautifulSoup 모듈을 사용합니다.
해당 페이지에서 원하는 텍스트에 검사를 클릭하면 해당 태그가 무엇인지 나온다.
이것의 아이디를 찾아서 soup.select("#아이디") 해주면 된다. 
하지만 id가 없는경우 불가능하다.
</pre>

<h2>main2.py - id가 없는 경우</h2>
<pre>
오른쪽마우스 검사를 클릭후 오른쪽마우스 copy -> copy selector를 클릭하여 복사한 후 사용한다.
css selector로 크롬이 자동 변환시켜준다. 이 셀렉터를 사용하면 id가 없어도 원하는 태그를
불러올 수 있다.
</pre>

<h2>main3.py - korbit api</h2>
<pre>
json으로 api를 값으로 불러오면 딕셔너리처럼 보이지만 문자로 취급함.
편하게 사용하고 싶으면 딕셔너리로 변환하면됨
- timestamp	최종 체결 시각
- last	최종 체결 가격
- bid	최우선 매수호가 (매수 수문 중 가장 높은 가격)
- ask	최우선 매도 호가 (매도 주문 중 가장 낮은 가격)
- low	최근 24시간 저가
- high	최근 24시간 고가
- volume	거래량
</pre>

<h2>main4.py - timestamp변환</h2>
<pre>
timestamp 항목은 최종 체결 시각을 의미하는데, 
일반적으로 1970년 1월 1일부터 지난 시간(초)을 의미합니다
편하게 읽으려면 datetime모듈을 사용해야한다.
</pre>