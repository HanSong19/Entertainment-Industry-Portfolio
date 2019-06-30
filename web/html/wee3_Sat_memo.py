1. to exit the file,
go to점프투 파이썬 -> 외장함수 and find 'sys'
python..py ~~~
right now, visal source code is executing ~~instead of us keep writing sys

sys.exit()

what is the difference between break and sys.exit()?
break is for exiting the for or while( ex, while True, for i in ~)
sys.exit() is for exiting the entire code that is running.

add following def to the code. 
def exit(self):
        while True:
            print("exit the program")
            sys.exit()

but, usually, make sure that you save everything before 

sys.path()
to check whether libraries are working

2. PICKLE

파일을 저장할때는 어떤 형식으로 저장할지 신경써야 한다.
특히, text일 경우에는 어떻게 객체화 할 것 인가
pickle은 객체를 형태를 그대로 저장 해두다가 부를수 있다.그래서 파이썬 내에서만 쓸때에는 pickle로 저장하면 편하다.
그러나 python에서 쓰고, java로 쓰던, Rscrip, C등에 나중에 쓸때에는 객체 그대로 저장하는 
방식은 잘 맞지않을 가능성이 많다, 그럴때는 jason을 쓰는것이 편하다.요즘 많이 쓰는 추세
csv.는 text기반 (,)로 text구분한다

2. 'wb'

wb는 text형태로 볼수 있는것 이외의 image, graph 등을 볼때 다 쓰면 된다.

3. OS
google-> python os library

4.Json
google Json
https://www.json.org/json-ko.html -> python -> The Python Standard Library
Json: 규칙을 따라야 하는 형식들을 모아둠/ 데이터를 교환하는 형식일뿐 프로그램이 아니다.
pickle 보다는 사람이 보기 더 용의하고 편하다. + 기계도 쉽게 읽을 수 있다.
Json은 언어로 부터 독립적, 그냥 그 언어가 json을쓸수 있는 library가 있을뿐
name/key 는 string만 되고
value 는 다른것이 다 올 수 있다.

 import json
dumps:
>>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
***-> 이거는 pyton의 형태인에 위에것을 실행하면은 Json형태로 바꾸어준다.

>>> import json
>>> print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
{
    "4": 5,
    "6": 7
}

***->indent=4 이걸 넣은 이유는 보기 편하게 하기 위해서

for related info,
google pyton list to json/ python dictionary to json etc.
http://pythonstudy.xyz/python/article/205-JSON-%EB%8D%B0%EC%9D%B4%ED%83%80

'wt' = write text

Picklerhk Json이 저장할때 차이점!
Pickle
pickle 
***-> pickle 은 데이터(객체)를 그대로 그냥 파일 (여기서는 f)로 바로바로 넣어서 저장
그래서 python안에서 저장하고 다시쓰기 좋음
Json
jsonString = json.dumps(customer)
***-> 이걸로 객체를 json형태로 저장을 한다. 그렇다고 이 형태를 파일로 저장 하는건 아님
그래서
with open("./python_basic_week3/test.json", 'wt') as f:
    f.write(jsonString)
***-> 파일 만들어서(여기서는 f), 여기에 write해주겠다는 두번째줄을 넣어야지만 f 파일에 저장이 된다
그리고 외부의 자료를 가져올때 보통 json을쓰기때문에 타 프로그램과 쓸때는 json을 더 많이 쓴다.

Json 은 그냥 객체를 text형태로 저장해 둔 것이다.
그래서 Json파일로 저장할때 ->incoding(dumps),
Json파일을 python에서 열어서 쓸때 -> decoding(load/loads)

dump/dumps 그리고 load/loads 차이 잘 알기




