import json,os
 

customer = {
    'id': 152352,
    'name': '강진수',
    'history': [
        {'date': '2015-03-11', 'item': 'iPhone'},
        {'date': '2016-02-23', 'item': 'Monitor'},
    ]
}
#json incoding
jsonString = json.dumps(customer)
 

print(jsonString)
print(type(jsonString))   

jsonString = json.dumps(customer, indent =4)
print(jsonString)

with open("./python_basic_week3/test.json", 'wt') as f:
    f.write(jsonString)

#json.dumps 파이썬 내에서 바로 사용 문자열, string과 연관이 있는 작업
jsonString = json.dumps (customer, indent = 4) 
print(jsonString)

#json.dump 파일로 바로 저장
with open("./python_basic_week3/test.json", 'wt') as f:
    json.dump(customer,f, indent = 4)

#json.loads json 문자를 읽어서 파이썬 객체로 변경
customer1 = json.loads(jsonString)
print(customer1)

#json.load json파일을 읽어서 파이썬 객체로 변경
with open("./python_basic_week3/test.json", 'wt') as f:
    customer2 = json.load(f)
    print(type(customer2))
    print(customer2)
'''

data = ['a','b',{1:'a',2:'b'}]

# dumps

json1 = json.dumps(data)
print(json1)

#dump

with open("./python_basic_week3/json_athome.json", 'wt') as f:
    json.dump(data, f, indent =4)

#loads

json2 = json.loads(json1)
[print(json2)]

#load

if os.path.exists ("./python_basic_week3/json_athome.json"):
    with open("./python_basic_week3/json_athome.json", 'rt') as json3:
        json3 = json.load(json3)
        print(json3)

