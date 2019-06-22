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