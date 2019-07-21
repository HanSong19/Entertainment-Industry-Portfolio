import urllib.request, time, json,db,pymysql
from bs4 import BeautifulSoup

params=urllib.parse.urlencode({'page':1})
url = "https://movie.naver.com/movie/point/af/list.nhn?&%s" %params
print(url)
response= urllib.request.urlopen(url)


navigator = BeautifulSoup(response,'html.parser')
table = navigator.find('table',class_='list_netizen')
print(table)
list_records = []


    
    
for i,r in enumerate(table.find_all('tr')): #i 는 tr의 인덱스값
    for j,c in enumerate(r.find_all('td')): #j는 td의 인덱스값
        if j==0:
            record = int(c.text.strip()) #j==1이 없는 이유는 별표는 지금 쓸 필요 없어서
        elif j==2:
            record1= int(c.text.strip())
        elif j==3:
            record2=str(c.find('a', class_='movie').text.strip())
            record3=str(c.text).split('\n')[2]
        elif j ==4:
            record4=str(c.find('a', class_ = 'author').text.strip())
            record5=str(c.text).split("****")[1]
    try:
        record_t=tuple([record,record1,record2,record3,record4,record5])
        list_records.append(record_t)
    except:
        pass
print(list_records)

conn= db.conn_db()
db.create_table()
db.insert_movie(list_records)








