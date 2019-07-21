import requests, selenium 
from bs4 import BeautifulSoup 

starbugs =requests.get('https://www.istarbucks.co.kr/store/store_map.do')
st_bs=BeautifulSoup(starbugs.text,'lxml') #이 라인이 조금 다르다, lxml도 parser와 비슷함
print(st_bs.select('li.quickResultLstCon'))

