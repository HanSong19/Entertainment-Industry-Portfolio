import csv
from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/Comparison_of_text_editors")
soup = BeautifulSoup(html, 'html.parser')

#class가 wikitable인 태그들 중에서 첫번째 태그 선택

table = soup.find_all('table',{'class':'wikitable'})[0]  #가장 처음 인덱스를 찾아서 넣어라/리스트로 저장됨
print(table)
print(type(table))
rows=table.find_all('tr')

#wt: 텍스트 쓰기 모드
csvFile = open('crawling/data/editors.csv','wt',newline = '', encoding='utf-8') #새라인 하나 띄우겟다

#csv파일 저장 객체
write=csv.writer(csvFile)
try:
    for row in rows:
        csvRow=[]
        #td,th 태그의 내용을 리스트에 추가
        for cell in row.find_all(['td','th']):
            csvRow.append(cell.get_text()) #여기까지오면 한줄로 저장/csv는 한건을 한 줄로 저장한다
        write.writerow(csvRow)
        #여기까지 오면 한줄이 저장 된 것이다. 그리고 다시 for문 들어가서 
finally:
    print('cvs로저장 되었습니다')
    csvFile.close()


