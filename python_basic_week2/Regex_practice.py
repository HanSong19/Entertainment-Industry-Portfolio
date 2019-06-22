'''
data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word [:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" +"*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n". join(result))
'''

#match

import re
'''
p = re.compile('[a-z]+') # +는 최소 하나만 있어도 된다. a-z 소문자 하나만
#있으면 된다
m = p.match("Python") #왜냐면 문자열의 가장 처음부터 가기때문에, 여기는 
#p가 대문자라서 none
print(m)

p = re.compile('[a-z]+') # +는 최소 하나만 있어도 된다. a-z 소문자 하나만
#있으면 된다
m = p.match("pyth0n 3") #p에서 h까지만 메치된다고 말해줌
print(m)
'''

#search
'''
p = re.compile('[a-z]+') 
m = p.search("python") 
print(m)

p = re.compile('[a-z]+') 
m = p.search("Python") #p이후 부터만 됨/ 꼭앞에서 부터 보지 않음(unlike match)
print(m)

p = re.compile('[a-z]+') 
m = p.search("3 pyth0n") #p이후 부터만 됨
print(m)
p.search()
'''
#fine all
'''
p = re.compile('[a-z]+') 
m = p.findall("3 Pyth0n") #이 패턴인것을 다 찾고 싶다
print(m)
'''
#finditer
p = re.compile('[a-z]+') 
m = p.finditer("as3 pyth0n") #이것이 iterator인가?
print(m)
for r in m: #iterator이면은 어디가 iterator인가?
    print(r)