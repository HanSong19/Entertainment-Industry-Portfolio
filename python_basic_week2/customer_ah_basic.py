# customer_at_home#
import re
custlist = []
page = -1
while True:
    menu = input('''
        I = 고객 정보 입력
        C= 현재/이전
        P= 이전 고객 정보 조회
        N= 다음 고객 정보 조회
        U= 고객 정보 수정
        D= 고객 정보 삭제(D)
        Q= 고객 정보 종료(Q)
    ''').upper()

    if menu == "I":
        customer = {'name':'', 'sex':'', 'email':'', 'birthyear':''}

        customer['name'] = input("please type your name: ")
        
        while True:
            customer["sex"]= input("please select your sex: ").upper()
            if customer["sex"] in ("F", "M"):
                break
            else:
                print("please select between 'm' and 'f': ")
        '''
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
        '''

        while True:
            emailcheck = re.compile('^[a-z0-9]+@[a-z]+[.][a-z]+$', re.I)  
            while True:   
                customer['email'] = input("please type your email: ")
                rightemail = emailcheck.search(customer['email'])
                if rightemail:
                    print("email is added")
                    break
                else: 
                    print("please type your email")

            check = 0            
            for i in custlist:
                if i['email'] == customer['email']:
                    check = 1
                    print("중복되는 이메일이 있습니다")
            if check == 0:
                break
                

        while True:
            customer["birthyear"] = input("please type the year of your birth: ")
            if len(customer["birthyear"]) == 4 and customer["birthyear"].isdigit():     
                break
            else:
                print("please write four numbers: ")
        print(customer)
        custlist.append(customer)
        page = page+1
        print(custlist)
        page = len(custlist)-1
        
    elif menu == "C":  
        if page >= 0:
            print("current page is {}".format(page+1))
            print(custlist[page])
        else:
            print("there is no information ")
    
    elif menu == 'P':
        if page >=1:
            print("The previous page is {}".format(page))
            print(custlist[page-1])
        else: 
            print("There is no previous page.")

    elif menu == "N":
        if page <= len(custlist)-2:
            print("the next page is {}".format(page+2))
            print(custlist[page+1])
        else:
            print("there is no next page")
    
    elif menu == "D":
        '''
        while True:           
            delcust = input("please enter the email address you want to delete: ")
            for i in custlist:
                delok=0
                if i['email'] == delcust:
                    delok =1
                    del i
                    print("it is successfully deleted")
                    print(custlist)
                    break
            if delok ==0:
                print("the information does not exist")
                break
        break
        '''
    
        delemail = input("please enter the email address you want to delete: ")
        delok = 0
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == delemail:
                delok=1
                print("{}'s information is deleted".format(custlist[i]['name'])) 
                del custlist[i]
                
                print(custlist)
                page= len(custlist)-1
                print(page)
                break
        if delok ==0:
            break

    elif menu == "U":
        while True:
            idx = -1
            exitinfo = input("if you do not want to change anything, type 'exit'/ if you want to change more, type 'change'")
            if exitinfo == 'exit':
                break
            elif exitinfo == 'change':
                identinfo = input("please write the email you want to change: ")
            
            for i in range(0,len(custlist)):
                if custlist[i]['email'] == identinfo:
                    changeinfo = input('''
                        please choose the information you want to change:
                        'name', 'sex','email', 'birthyear'
                        if you don't want to change, type 'exit
                        ''')
                    if changeinfo in ('name', 'sex','email', 'birthyear'):
                        custlist[i][changeinfo] = input("how do you want to change?: ")
                        idx += 1
                        print(custlist[i])
                        break
            if idx == -1:
                break

    elif menu == 'Q':
        print("exit the program")
        break
    
    else:
        print("choose among options")
        break
            

                
                    

    
     