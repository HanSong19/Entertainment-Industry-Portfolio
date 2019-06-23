class Cookie:
    pass

a = Cookie()
b = Cookie()

print(type(a))
print(type(b))

class FourCal: #camel type
    first = 0
    second = 0 #파이썬은 자동으로 변수 선언을 해서 굳이 이 두줄 안적어도 됨
    def setdata(self, first, second): 
    #self: class안의 함수를 할때, parameter안에는 무조건 self를 써야한다. 그러나 실제 쓰지는 않는다
        self.first = first #self 가 붙으면 class가 가진 first. 그냥 first = parameter의 first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first + self.second
        return result


    def sub(self):
        result = self.first - self.second
        return result

    
    def div(self):
        result = self.first / self.second
        return result



c = FourCal() # c is the instance of Class FourCal, but actually it has the address of
              #class FourCal.
d = FourCal() #c and d are two different instances
c.setdata(5,7)
d.setdata(3,4)
print(c.first)
print(c.second)

#밖에서 클라스 안의 함수의 parameter을 지정 할때#
c.first = 10
c.second = 20

print(c.first)
print(c.second)



d.setdata(3,4)
#id: where is the a
print(id(c), id(c.first))
print(id(d), id(d.first))


# sum
sumresult = c.add()
print(sumresult)
    
#rest

print(c.mul())
print(c.sub())
print(c.div())


##Constructor
'''
만들면서 이미 기본값을 설정해 두고 싶을때 
'''
class FourCal2: #camel type
    def __init__(self, first, second): #def __init__(self, first=0, second=0): 하면 값없이도 나옴 오류없이\
                                       #안들어오면 Default로 이 값을 쓴다.
        self.first = first
        self.second = second

    def setdata(self, first, second): 
    #self: class안의 함수를 할때, parameter안에는 무조건 self를 써야한다. 그러나 실제 쓰지는 않는다
        self.first = first #self 가 붙으면 class가 가진 first. 그냥 first = parameter의 first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first + self.second
        return result


    def sub(self):
        result = self.first - self.second
        return result

    
    def div(self):
        result = self.first / self.second
        return result


aa = FourCal2(1,2)
print(aa.add())

class safeFourCal2(FourCal2):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


aa = FourCal2(4,0)
bb = safeFourCal2(5,0)
print(bb.div())

class M :
    class_V = 0

aaa= M()
bbb = M()
print(aaa.class_V)
print(bbb.class_V)

M.class_V = 5
print(aaa.class_V)
print(bbb.class_V)

aaa.class_V = 6
print(aaa.class_V)
print(bbb.class_V)
