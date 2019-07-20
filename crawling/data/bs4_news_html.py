import urllib.request, time
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/list.nhn?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y"
response= urllib.request.urlopen(url)
res= response.read()

soup = BeautifulSoup(res,'html.parser')
keywords = soup.find_all('a', class_='nclicks(cnt_flashart)')
keywords2 = soup.find_all('a', class_='nclicks(fls.list)')
results = keywords+keywords2


#keywords = [each_line.get_text().strip() for each_line in results]
#get_text: 문자열만 추출한다, strip(): 공백을 제거 하겠다
print(results)

for result in results:
    #for i in len(results):
        #print("제목: ", results[i])
    print("제목: ",result.string)
    print("링크: ", result.attrs['href'])
    print()
    url_content = result.attrs['href']
    response_content = urllib.request.urlopen(url_content)
    soup_content = BeautifulSoup(response_content,'html.parser')
    content = soup_content.select_one('#articleBodyContents')

    output=''
    for item in content.contents:
        stripped = str(item).strip()
        if stripped=='':
            continue
        if stripped[0] not in ['<','/']:
            output+=str(item).strip()
    output = output.replace('무단 전재 및 재배포 금지','')
    output = output.replace('본문 내용tv플레이어','')
    print(output)
    print()

    time.sleep(3)

