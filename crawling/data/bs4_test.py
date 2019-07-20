#always import soupf first
from bs4 import BeautifulSoup

#beautiful soupd 의 quick start에서 밑에를 다 복사하기
'''
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister " id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
#soup = BeautifulSoup(html_doc,'html.parser')
#html_doc이거는 html테그안에 들어있는 모든것이다 ex) head, body ect.

#print(soup.prettify())
#prettify 는 예쁘게 만들어 준다/ 가독성 있게 


print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find_all(id="link3"))

for link in soup.find_all('a'):
    print(link.get('href'))

a=soup.get_text()
#print(a)
#print(type(a)) 

tag = soup.a
#print(type(tag))
#print(tag.name)
tag.name = "blockquote"
#print(tag.name)

#전체를 다 찍고 싶을때, 보면 a tag중 하나가 blockquote로 바껴 있다
#print(soup)


print(tag['id'])
print(tag.attrs)
#atts는 dictionary로 나온다, 그래서 이용 할때는 그림이나 글짜에 링트가 걸려 있을때 그걸 클릭하면 
#내용이 있다, 그러니까 링크안에 그 다음페이지로 가는 url이 있으니까 타고 들어가서 글자나 제목을 가져 올 수 있다.


tag['id'] = 'verybold'
#tag[id] 바꾸는것
tag['another-attribute']=1
#tagd의 id 추가 하는것
print(tag)
print(soup)

tag['id']
print(tag.get('id'))

#att1=soup.a['class']
#print(att1)

rel_soup = BeautifulSoup('<p>Back to the <a rel = "index">homepage</a></p>')
#print(rel_soup.a['rel'])
#rel_soup.a['rel'] = ['index', 'contents']
#print(rel_soup.p)

print(rel_soup.prettify())
tag = rel_soup.a
print(tag.string)
print(type(tag.string))
tag.string.replace_with("no longer bold")
print(tag)
'''
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
tag=soup.p
#print(tag.contents)
tag1=soup.body
#print(tag1.contents[5])
#print(len(tag1.contents))

#for child in tag1.children:
#    print(child)


print(len(list(tag1.children)))
print(len(list(tag1.descendants))) #descendants 는 안에 내용이 몇개나 얼마나 있는지 체크한다


html ='''
<html>
<body>
<div id ="main-goods" role ="page">
    <h1>과일과 야채</h1>
    <ul id = "fr-list" class = "items art it book">
     <li class = "red green" data-lo="ko">사과</li>
     <li class = "red green" data-lo="ko">포도</li>
     <li class = "red green" data-lo="ko">레몬</li>
     <li class = "red green" data-lo="ko">오렌지</li>
    </ul>
</div>
</body>
</html>
'''
soup = BeautifulSoup(html,'html.parser')
header=soup.select_one('body div h1')
list_items=soup.select('li:nth-of-type(3)')

print(header.string)
print(soup.select_one('ul').attrs)
print(list_items)
for li in list_items:
    print(li.string) 

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')