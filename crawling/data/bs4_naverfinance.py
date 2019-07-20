import urllib.request  #해당하는 문설를 읽어오는 역할
from bs4 import BeautifulSoup #필요한것들을 추출함

url = 'http://www.cgv.co.kr/movies/'
response = urllib.request.urlopen(url) #주소에 있는것을 읽어오기

soup = BeautifulSoup(response, 'html.parser') #지금은 url에 있는 것을 들고오니까 그냥 parser로 열면된다
results = soup.select('strong.title')  #span.tag안에 class가 value인것
                               #a em 은, a테그 밑에 클래스 말고 밑에 테그 가져오기

for result in results:
    print(result.string)
print(type(results))

print("#1 movie:",results[0].string)






