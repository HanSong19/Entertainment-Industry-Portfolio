import urllib.request  
from bs4 import BeautifulSoup 

url = 'https://music.bugs.co.kr/chart'
response = urllib.request.urlopen(url) 

soup = BeautifulSoup(response, 'html.parser') #지금은 url에 있는 것을 들고오니까 그냥 parser로 열면된다
results = soup.select('th>p>a')  # a태그 안 내용에 있느니까, 이 내용만 가져올 특별한 루트를 가져오면 된다, 여기서는 테이블 안에 p 안에 a 안의내용이니까 바로바로 밑으로 >쓰면됨
                                 # 아니면 th p a 로 spacebar로 나눠줘도 된다

for result in results:
    print(result.string)
print(type(results))

print("#1 movie:",results[0].string)






