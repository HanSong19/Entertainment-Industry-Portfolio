treeHit = 0
while treeHit<10:
    treeHit = treeHit+1
    print("나는 나무를 %d 번 찍었습니다" % treeHit)
    if treeHit == 10:
        print("나무가 넘어 갑니다")

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit

Enter number:"""

number = 0
while number != 4:
    print(prompt)
    number = int(input())

#만약에 error가 뜨고 invalid가 뜬다면
'''
number = 0
while number != '4':  # 4를 숫자말고 '4'해서 string으로 인지하게 한다
    print(prompt)
    number = input() #int를 빼고 그냥 input을 쓴다 bc, input은 string 받기때문
'''
#practice 'break'
coffee = 5
money = 5
while money:
    print("coffee will come soon")
    coffee = coffee-1
    if coffee == 0:
        print("we ran out of coffee")
        break

#practice 'continue'
a = 0
while a<10:
    a= a+1
    if a%2 == 0: continue
    print(a)

while True:
    print("Ctrl+C를 눌러야 while")
