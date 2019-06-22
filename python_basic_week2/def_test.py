import re
def add(a,b):
    result = a+b
    print("a=",a, "b=",b)
    return result

# print(add(b=5, a=4))= print(add(4,5))
print(add(b=5, a=4))

def add_many(*args): #()안에 몇개가 들어오든 상관 없다
    result = 0
    for i in args:
        result += i
    return result
print(add_many(1,2,3,4,5,6,7,8,9,10))

def print_kwargs(**args):
    print(args)

print_kwargs(name = '한별', age = '29', city = 'busan')

#global

a= 1
def test_1(a):
    a=a+1  ##함수안의 a와 밖의a는 완전히 다른 함수 이다
    
test_1(a)
print(a)


def test_2():
    global a
    a=a+1

test_2()
print(a)

