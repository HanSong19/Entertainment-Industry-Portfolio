import re
custlist = []
page = -1

while True:
    choice = input('''
    다음중 하실 일을 골라주세요
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()

    if choice == "I":
        customer = {'name':'', 'sex':'', 'email':'', 'birthyear':''}

        customer['name'] = input("이름을 입력해 주세요: ")

        while True:
            customer['sex'] = input("성별을 입력 하시오: ")
            customer['sex'] = customer['sex'].upper()
            if customer['sex'] in ('M','F'):
                break
        
        while True: #중복되지 않게

            regex = re.compile('^[a-z][a-z0-9]{4,10}@[a-zA-Z]{2,6}[.][a-zA-Z]{2,3}$')
            while True: #반복해서 원하는 값을 계속해서 얻어야 해서
                customer['email']= input("이메일을 입력하세요")
                golbang = regex.search(customer['email'])
                if golbang:
                    break
                else:
                    print("'@'를 포함한 정확한 이메일을 써주세요.")
            check = 0 
            for i in custlist:
                if i['email'] == customer['email']:
                    check=1
            if check == 0:
                break
            print("중복되는 이메일이 있습니다")

        while True:
            customer['birthyear'] = input("출생년도 4자리를 입력해주세요: ")

            if len(customer['birthyear']) == 4 and customer['birthyear'].isdigit():  #.isdigit(): 숫자로 되어 있는가 확인하는 함수
                break
        print(customer)
        custlist.append(customer)
        print(custlist)
        page = len(custlist)-1
    elif choice == "C":
        print("현재 고객 정보 조회")

        if page >= 0:
            print("현재 페이지는 {}쪽 입니다".format(page+1))  #여기 페이지는 인덱스 값이다, 그래서 +1
            print(custlist[page]) #여기는 그대로 인덱스 값넣으면 됨 -> 딕셔너리 통채로 나온다
        else: # = 'page=-1' 이라는 뜻이다
            print("입력된 정보가 없습니다")
        #내가쓴답#
        '''
        for i in custlist:
            if custlist.index[i] => 1:
                print(custlist[i-1])
            elif custlist.index[i] =0:
                print(custlist[i])
            else:
                print("no customer information")
        '''
    elif choice == "P":
        print("이전 고객 정보 조회")
        if page <= 0:
            print("첫번째 페이지라 이전 페이지로 이동이 불가 합니다")
            print(page)
        else:
            page -= 1
            print("현재 페이지는 {}쪽 입니다".format(page+1))
            print(custlist[page])
        #내가 쓴 값
        '''
         for i in custlist:
            if custlist.index(i) > 0:
                print(custlist[i-1])
            elif: custlist.index(i) <= 0:
                print("there is no customer before")
        '''
    elif choice == "N":
        print("다음 고객 정보 조회")

        if page >= len(custlist)-1:
            print("마지막 페이지라 다음 페이지로 이동이불가")
            print(page)
        else:
            page +=1
            print("현재 페이지는 {}쪽 입니다".format(page +1))
            print(custlist[page])
        #내가 한답#
        '''
        a= len(custlist) -1
        for i in custlist:
            if i> a:
                print(custlist[i])
            else:
                print("there is no next customer")
        '''    
    elif choice == "U":
        print("고객 정보 수정")
        while True:
            choice1 = input("수정하시려는 고객 정보의 이메일을 입력하세요: ")
            idx = -1
            for i in range(0,len(custlist)):
                if custlist[i]['email'] == choice1:
                    idx = i
                    break #for문을 벗어나는 break
            if idx ==-1:
                print("등록되지 않은 이메일입니다")
                break #while 문을 벗어나는 break
            choice2 = input('''
            다음중 수정하실 정보를 골라주세요
                name, sex, birthyear
            (수정할 정보가 없으면 'exit' 을 입력)
            ''')
            if choice2 in ('name','sex','birthyear'):
                custlist[idx][choice2] = input("수정할 {}을 입력하세요:".format(choice2))
                break
            elif choice2 == 'exit':
                break
            else:
                print("존재하지 않는 정보 입니다.")
                break

        #내가 한 답
        '''
        custemail = input("변경하고싶은 고객 정보의 이메일을 입력하세요.")
        amend = 0
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == custemail:
                amendinfo = input("어느 정보를 수정하고 싶은가요? name/sex/email/birthyear")
                if amendinfo == 'name':
                    amendname = input("새 이름을 입력하세요")
                    custlist[i]['name'] = amendname
                elif: amendinfo == 'sex'
                    amendsex = input("새 성을 입력하세요")
                    custlist[i]['sex'] = amendsex
                elif: amendinfo == 'email':
                    amendemail = input("새 이메일을 입력하세요")
                    custlist[i]['email'] = amendemail
                else:
                    amendbirthyear = input("새 탄생년도를 입력하세요")
                    custlist[i]['birthyear'] = amendbirthyear
        :
            break
            '''
    elif choice == "D":
        choice1 = input("삭제하려는 고객 정보의 이메일을 입력하세요.")
        delok = 0
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:   ##while을 쓰면은 꼭 밑에 break가 있어야하고 while대신 if쓰면 밑에 break 지워도됨
                print('{}고객님의 정보가 삭제 되었습니다.'.format(custlist[i]['name']))
                del custlist[i]
                print(custlist)
                page = len(custlist)-1
                print(page)
                delok = 1
                break
        if delok == 0: #custlist 안을 다 체크 해봤는데 그래도 email이없다 그러면 여기에 걸린다
            print("등록되지 않은 이메일입니다")
            print(custlist)    
    elif choice == "Q":
        print("프로그램 종료")
        break
    else:
        print("잘못 입력 하셨습니다.")
    


        