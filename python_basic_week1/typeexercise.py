##type exercise##
'''
import random, time
words = ["apple","bee","pencil","butterfly","cup","brush"]
correct = 0
wrong = 0
input("press 'enter' when you are ready to start")
print("starting now!")
start = time.time()
while correct != 5:
    a= random.randint(0,5)
    print(words[a])
    answer= input("")
    if answer == words[a]:
        correct += 1
        continue
    else: 
        wrong += 1
end = time.time()
et= end-start
print("you took %d seconds to finish"%et)
'''

##답##
'''
import random, time
n=1
w= ['cat','dog','fox','monkey','panda','frog', 'snake','wolf']
q=random.choice(w)
input("시작")
start = time.time()
while n<=5:
    print("*문제",n) #문제1,2,3, 으로 나온대 그래서 위에 n=1부터 시작함
    print(q)
    x=input()
    if q ==x:
        print("pass")
        n=n+1
        q=random.choice(w)
    else:
        print("try again")
end = time.time()
t = end-start
print("the time you tood is {:.0f} seconds".format(t))
'''

## read words from file and run the course
import random, time
n=1
w= ['cat','dog','fox','monkey','panda','frog', 'snake','wolf']

while True:
    print("1.문제 불러오기 2. 타자게임 3. 종료하기")
    menu = input("메뉴를 선택하시오\n")
    if menu == '1':
        r = open("./python_basic/words.txt","r")
        line = 1
        while line:
            line = r.readline(). replace("\n","") # 뒤에 앤터키 친것을 빈 문자로 바꾸어준다
            if not(line ==''):
                w.append(line)
        print(w)
    elif menu == '2':
        q=random.choice(w)
        input("시작")
        start = time.time()
        while n<=5:
            print("*문제",n) #문제1,2,3, 으로 나온대 그래서 위에 n=1부터 시작함
            print(q)
            x=input()
            if q ==x:
                print("pass")
                n=n+1
                q=random.choice(w)
            else:
                print("try again")
        end = time.time()
        t = end-start
        print("the time you tood is {:.0f} seconds".format(t))
    elif menu == '3':
        break
