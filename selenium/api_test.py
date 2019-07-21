#BAJ7i6KRlmHygpSMbzya
#gquDDmHuF0


import os
import sys
import urllib.request
client_id = "BAJ7i6KRlmHygpSMbzya"
client_secret = "gquDDmHuF0"
encText = urllib.parse.quote("다나스")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과/ movie 에서 찾고 싶으면 search/movie, 뉴스에서 찾고 싶으면 search/news?하면 된다
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)