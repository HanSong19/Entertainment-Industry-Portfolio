##type exercise##
import random, time
words = ["apple","bee","pencil","butterfly","cup","brush"]
correct = 0
wrong = 0
while correct != 5:
    a= random.randint(0,5)
    print(words[a])
    answer= input("")
    start = time.time()
    if answer == words[a]:
        correct += 1
        continue
    else: 
        wrong += 1
end = time.time()
et= end-start
print("you took %d to finish"%et)


