import re

class customer ():
    custlist = []
    page = -1


    
    def customerinput(self):
        
        customer = {'name':'', 'sex':'', 'email':'', 'birthyear':''}

        customer['name'] = input("please type your name: ")
        
        while True:
            customer["sex"]= input("please select your sex: ").upper()
            if customer["sex"] in ("F", "M"):
                break
            else:
                print("please select between 'm' and 'f': ")
        
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
            for i in self.custlist:
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
        self.custlist.append(customer)
        print(self.custlist)
        self.page
        self.page = len(self.custlist)-1

    def currentinfo(self):
        self.page
        if self.page >= 0:
            print("current page is {}".format(self.page+1))
            print(self.custlist[self.page])
        else:
            print("there is no information ")

    def previousinfo(self):
        self.page
        if self.page >=1:
            print("The previous page is {}".format(self.page))
            print(self.custlist[self.page-1])
        else: 
            print("There is no previous page.")

    def nextinfo(self):
        self.page
        if self.page <= len(self.custlist)-2:
            print("the next page is {}".format(self.page+2))
            print(self.custlist[self.page+1])
        else:
            print("there is no next page")

    def changeinfo(self) :
        while True:
            idx = -1
            exitinfo = input("if you do not want to change anything, type 'exit'/ if you want to change more, type 'change'")
            if exitinfo == 'exit':
                break
            elif exitinfo == 'change':
                identinfo = input("please write the email you want to change: ")
            
            for i in range(0,len(self.custlist)):
                identinfo = input("please write the correct email you want to change: ")  
                if self.custlist[i]['email'] == identinfo:
                    changeinfo = input('''
                        please choose the information you want to change:
                        'name', 'sex','email', 'birthyear'
                        if you don't want to change, type 'exit
                        ''')
                    if changeinfo in ('name', 'sex','email', 'birthyear'):
                        self.custlist[i][changeinfo] = input("how do you want to change?: ")
                        idx += 1
                        print(self.custlist[i])
                        break
                else:
                    print("please write the correct email you want to change: ")  
            if idx == -1:
                break

    def deleteinfo(self):
        self.page
        delemail = input("please enter the email address you want to delete: ")
        delok = 0
        for i in range(0,len(self.custlist)):
            if self.custlist[i]['email'] == delemail:
                delok=1
                print("{}'s information is deleted".format(self.custlist[i]['name'])) 
                del self.custlist[i]
                
                print(self.custlist)
                page= len(self.custlist)-1
                print(self.page)
                break
        if delok ==0:
            print("there is no emial found")
            
    def exit(self):
        while True:
            print("exit the program")
            break

    def firstchoice(self):
    
        menu = input('''
            I = 고객 정보 입력
            C= 현재/이전
            P= 이전 고객 정보 조회
            N= 다음 고객 정보 조회
            U= 고객 정보 수정
            D= 고객 정보 삭제(D)
            Q= 고객 정보 종료(Q)
        ''').upper()
        return menu   
    
    def exe(self, menu):
        if  menu == 'I':
            self.customerinput()

        if menu == 'C':
            self.currentinfo()

        if menu == 'P':
            self.previousinfo()

        if menu == 'N':
            self.nextinfo()

        if menu == 'U':
            self.changeinfo() 

        if menu == 'D':
            self.deleteinfo()

        if menu == 'Q':
            self.exit()

    def __init__(self):
        while True:
            m= self.firstchoice()
            self.exe(m)
customer()

