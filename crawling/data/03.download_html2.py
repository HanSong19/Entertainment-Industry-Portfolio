import urllib.request
import urllib.parse

#https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%B4%88%EC%BD%9C%EB%A6%BF
#https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%9E%A5%EB%A7%88
api = 'https://search.naver.com/search.naver'

values ={
    'where': 'news',
    'sm' : 'tab_jum',
    'query': '장마'
}

params = urllib.parse.urlencode(values)
print(params)
#parse 가 형태를 맞춰주는 역할도 한다
url = api+'?'+params 
print(url)
#여기까지는 요청할 주소 값을 맞춘 것이다

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8') #마약에 decoding이 안맞으면 utf-8대신에 다른 decoding을 넣으면 된다
print(text)
