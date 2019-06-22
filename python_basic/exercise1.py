## 주민번호 성별 체크
'''
a=input("주민번호 입력:") #input은 string으로 받아들이기때문에 index쓸수 있다
#사용자가 무언가를 치면 답이 나오는 것을 원하면 input()
if a[7]=='1' or a[7] =='3':
    print("male")
elif a[7] =='2' or a[7]== '4':
    print("female")
'''

## 2~9 구구단 출력하기 세로로
'''
for i in range(1,9):
    print("2 x i = 2*i")

 #답
 #고정되는 값은 밖에(단), 변하는 값(곱하기하는값) 은 안에
for x in range(2,10):
    print("\n--[%d단])--" %x) #\n: 줄 바꾸기
    for y in range (1,10):
        print("%d x %d = %d" %(x,y,x*y))
'''
## 2~9 구구단 출력하기 가로로 내답
'''
for x in range(2,10):
    for y in range (1,10):
        print("%d x %d = %d" %(x,y,x*y))
'''
#답
'''
for x in range(1,10): #이번에는 단이 밖에 온다, 처음 라인에 다 x1이니까
    for y in range(2,10):
        print("%d x %d = %2d" %(y,x,x*y), end = '  ') # option1:2d 는 숫자가 10 자리로
        #넘어가면 자리 맞추기 위해서, end = '   '원래 기본값이 다음 라인으로 넘어가는
        #데 그거 대신에 그냥 자리 줘라
        #print("{} x {} = {:2}".format(y,x,x*y), end='  ') #option 2: {:2}는 두자리 공간중에 두번째 
        #자리에 맞추어서 쓰라는 것, 10 이상되는 수와 자리 맞추기 위해서
    print()#줄바꾸는 역할
'''
#coffee
'''
coffee = {'카페라떼':3000, '아메리카노':2000, '모카':3500}
for c in coffee: # list all the keys in coffee, only keys here
    print(c, end=' ')
print() #move to the next line

order = input("choice: ")
for k,v in coffee.items(): #coffee에있는 거랑 order랑 비교, 여기서는
#key 랑 value다 필요한데 이때 .items()쓰면 키랑 벨류 다 나옴 for k 가
#앞에잇어서 키 v가 뒤에 있어서 벨류
    if k == order:
        print(v)
# if I want to make extra menu for the machinem, I can use
#add and delte of dicitonary
'''

##덧셈 문제 
# What I tried: to add random, I need below
'''
import random
a= random.randint(1,50)
b=0
for i,j in a:
    input("i + j = ")
    for x in range(1,11):
        b= b+1
        if b<10 and input == i+j:
            print('정답!')
        elif b==10:
            print("10개 맞음")
'''

# 답
'''
import random
count=0
for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    print("%d + %d = " %(a,b))
    c=int(input())
    if a+b ==c:
        print("정답!")
        count+=1
    elif a+b!=c:
        print("오답")
print("%d 개 맞음"%count)
'''

##사칙연산 using eval() in 내장 함수
import random
'''
oper = ['+','*','%','-']
count = 0
for x in range (0,3):
    a=random.randint(1,50)
    b=random.randint(1,50)
    c=random.choice(oper)
    if c == '+':
        print("%d + %d= " %(a,b))
        d=int(input())
        if a+b ==d:
            print("정답!")
            count+=1
        else:
            print("오답")
    elif c == '*':
        print("%d * %d= " %(a,b))
        d=int(input())
        if a*b ==d:
            print("정답!")
            count+=1
        else:
            print("오답")
    elif c == '-':
        print("%d - %d= " %(a,b))
        d=int(input())
        if a-b ==d:
            print("정답!")
            count+=1
        else:
            print("오답")
    elif c == '%':
        print("%d + %d= " %(a,b))
        d=int(input())
        if a%b ==d:
            print("정답!")
            count+=1
        else:
            print("오답")
print("%d 개 맞음"%count)
'''

#답
'''
count = 0
oper = oper = ['+','*','/','-']
for x in range(0,5):
    a=random.randint(1,50)
    b=random.randint(1,50)
    op=random.choice(oper) #random.coice() allows me to choose whatever is in 
    #the list, .randint() onlw shows integers
    quiz=str(a)+op+str(b)
    print(quiz, '=') #if there is a ',' in print, it shows with one space
    print(eval(quiz))
    c=int(input('정답='))

    if int(eval (quiz))==c: #there is int() because소수 가 있을수있다 나누기때문에
        print("정답!")
        count+=1
    else:
        print("오답!")
print("%d 개 맞음"%count)
'''

#timer
'''
import keyboard
while True:
    if keyboard.is_pressed
'''

#답
'''
import time
input ("엔터키를 누르고 20초를 세시오") #인풋은 계속 대기할 수 있다
start = time.time()
input("20초 후 다시 엔터키를 누르시오")
end = time.time()
et = end - start
print("실제시간 :", et, "초")
print("차이 :", abs(et -20), "초") #abs removes - or + 절대값 화한다
'''
###숫자 맞추기
'''
import random
count = 0
a= random.randint(1,100)
print(a)
while True:
    b=int(input("please select a number btw 0-100: \n"))
    count+=1
    if a>b:
        print("select a bigger number")
    elif a<b:
        print("select a smaller number")
    elif a==b:
        print("that's the correct number")
        break
'''
##답
'''
import random, time

com=random.randint(1,100)
count=0
print("답 : ", com)## shows the answer just to check the code
input("시작!")
start = time.time()
while True:
    input_no = int(input('1~100사이 숫자를 입력하시오\n'))
    count+=1 #어차피 전부다 필요하니까 맨 위에 써주면된다
    if com == input_no:
        print('정답입니다. {} 번만에 맞추셨습니다.'.format(count))
        break
    elif com>input_no:
        print('더 큰수를 입력하세요')
    else:
        print('더 큰수를 입력하세요')
end = time.time()
t=end-start
print('걸린 시간은 {:.0f}초 입니다.'.format(t))
'''
###로또번호생성
'''
import random
num = random.randint(1,45)
a= []
for i in range(1,5):
    num = random.pop(45)
    return a.pop(num)

'''
#answer 1
'''
import random
for i in range(5): # = range(0,4)
    lotto = [0,0,0,0,0,0]
    for x in range(6):
        num=0
        while(num= in lotto):
            num=random.randint(1,46)
        lotto[x]=num
    print("로또 : ", sorted(lotto))
'''
#answer2
'''
import random
for i in range(5):
    print("로또 ;" , sorted(random.sample(range(1,46),6)))
'''
##야구게임
'''
import random
num = random.sample(range(1,9),3)
count=0
while True:
    input_num= int(input("plz select three numbers: "))
    count+=1
    if input_num == num:
        print("strike")
    elif input_num == 
'''

## the answer
import random
com = random.sample(range(1,10),3)
print(com)
strike = 0
check = 0
print("시작")
while strike !=3:
    strike = 0
    ball = 0
    guess = list(input("3자리 숫자를 입력하세요: ")) # str ['7','8','9']로 되잇다
    print(guess)
    for a in guess: #ex) 7 을 가져온다
        for b in com: #ex) 위의 7 을 com에 있는 1,2,3 모두와 비교한다
            if int(a) == b:
                if guess.index(a) == com.index(b):
                    strike+=1
                else:
                    ball+=1
    check+=1
    print("스트라이크: %d, 볼: %d, 시도횟수: %d" %(strike, ball,check))
print("정답")











