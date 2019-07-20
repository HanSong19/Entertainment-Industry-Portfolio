import urllib.request
from bs4 import BeautifulSoup

url = "https://www.naver.com/"
response= urllib.request.urlopen(url)
res= response.read()

soup = BeautifulSoup(res,'html.parser')
keywords = soup.find_all('span', class_='ah_k')

keywords = [each_line.get_text().strip() for each_line in keywords[:20]]
#get_text: 문자열만 추출한다, strip(): 공백을 제거 하겠다
print(keywords)

for key in keywords[:20]:
    print(key)
    
#아니면 이렇게 해도 같은 답이 나온다
