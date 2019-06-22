#baseball
import random

comnum = random.sample(range(1,10),3)
print(comnum)
strike = 0
count = 0

while strike != 3:
    strike = 0
    ball = 0
    guessnum = list(input("please choose three numbers: "))
    print(guessnum)
    for i in guessnum:
        for j in comnum:
            if int(i) == j:
                if guessnum.index(i) == comnum.index(j):
                    strike += 1
                else:
                    ball+= 1
    count+= 1    
    print("you have {} strike(s), {} ball(s), and tried {} times,".format(strike, ball, count))

 