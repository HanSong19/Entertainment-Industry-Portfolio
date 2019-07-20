import urllib.request

url = 'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=011&aid=0003589540'

mem=urllib.request.urlopen(url).read()
print(mem)
#print(mem.decode("utf-8"))

