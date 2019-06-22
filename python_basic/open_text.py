#create a file and write in it##
'''
f= open("./python_basic/word.txt","w")
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close
'''
#append
'''
f= open("./python_basic/word.txt","a")
for i in range(11,20):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close
#read file
#readliine
'''
'''
f= open("./python_basic/word.txt","r")
while True: #무한하게 반복
    line = f.readline()
    if not line: break
    print(line)
f.close()
'''
#readlines/ sees like the same was as above, but faster and less memory
'''
f= open("./python_basic/word.txt","r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()
'''

