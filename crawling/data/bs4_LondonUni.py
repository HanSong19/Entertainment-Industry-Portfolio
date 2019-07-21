import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://en.wikipedia.org/wiki/List_of_universities_and_higher_education_colleges_in_London")
soup = BeautifulSoup(html,'html.parser')

table = soup.find_all('table',{'class':'wikitable'})[0]
rows = table.find_all('tr')

csvFile = open('crawling/data/LondonUni.csv','wt', newline = '', encoding ='utf-8')

write=csv.writer(csvFile)

try:
    for row in rows:
        csvRow=[]
        for cell in row.find_all(['td','th']):
            csvRow.append(cell.get_text())
        write.writerow(csvRow)

finally:
    print('csv로 저장 되었습니다')
    csvFile.close()
