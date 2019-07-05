
import sys, pickle
'''print(sys.path)

import pickle  ##객체를 그대로 저장하고 불러와서 쓸 수 있는것이 pickle의 가장 큰 장점이다
data = {1:'python', 2:'you need'}
#type dict
print(type(data))

#파일로 저장 
with open ("./python_basic_week3/test.pickle", 'wb') as f:
    pickle.dump(data, f)

#파이썬 내에서 사용 바이트 형태/ 's'붙은 것은 문자열을 읽고 쓰고 가능/ byte 기반
datab = pickle.dumps(data)
print(type(datab))

#파이을 읽어옴
with open ("./python_basic_week3/test.pickle", 'rb') as f:
    data = pickle.load(f)
    print(data)

#바이트 타입을 파이썬 형태의 데이타 타입으로
data1 = pickle.loads(datab)
print(data1)
print(type(data1))
'''

f= open("./python_basic_week3/pickle_test_ah.py",'wb')
data = [{'a':1, 'b':2}, 'apple', 'bee']
pickle.dump(data,f)
f.close()

f=open("./python_basic_week3/pickle_test_ah.py", 'rb')
pickle.load(f)
print(data)