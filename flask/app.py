from flask import Flask, render_template, request
app = Flask(__name__)
#요청 들어오면 돌려보내줄 route를 다 만들어 놓는다#
@app.route("/") #.com/ 이후(거의 첫번째 페이지에)에서 뭔가 요구하면은 다음을 보여 주겠다
def index(): #보통 별다른 요청 없이 들어오는 페이지를 index.jsp등으로쓰기 때문에 그냥 index라고 이름을 주로 잡는다, 함수 이름이 중복되면 안됨
    return "hello world" #이것을 그러면 response에 실어서 사용자(client)에게 보내준다

@app.route('/cakes') #그 주소값 뒤에 /cakes를 치면 yammy cakes! 가 나온다
def cakes():
    return "Yummy cakes!"

@app.route('/user/<username>') #127.0.01:5000/user/han하면 결과나온다
def user(username):
    return "User %s"%username

@app.route('/user/<username>/<int:age>') #127.0.01:5000/user/han/29하면 결과나온다
def user1(username, age):
    # return "Username %s, age %d"%(username, age) (template 안쓰고 바로 get할때)
    return render_template ('index.html',username=username, age=age)# render_template 통해서 하는 방법 127.0.01:5000/user/han/29하면 결과나온다
@app.route("/forminput/") # 주소 + /forminput먼저 해야 다음꺼 나옴
def forminput():
    return render_template ("forminput.html") #이거는 가서 그냥 submit버튼만 실행하고 맨윗줄 실행하고 옴
    #그래서 바로밑에 route로 해줘야함
    
@app.route("/method/", methods = ["GET","POST"])
def method():
    if request.method == "POST":
        return "post"
    else: 
        return "get"
@app.route("/login/") #method 안적엇으니까 default 로 get이다
def login():          #http://127.0.0.1:5000/login/?name=han
    username = request.args.get("name")  ##get방식은 args에 있고, post방식은 form 에 있다
    return render_template('index.html', username = username)

@app.route("/forminput1/") # 주소 + /forminput먼저 해야 다음꺼 나옴
def forminput1():
    return render_template ("forminput1.html") 

@app.route("/login/", methods = ['POST']) 
def login_post():          #http://127.0.0.1:5000/login/?name=han
    username = request.form['username']
    password= request.form['password']
    return render_template('index.html', username = username, password = password)


if __name__ == '__main__': #원래 함수는 호출하기전에 실행이 안되는데 run은 이것들을 다 실행 해버리는 것이다. 다른파일에서 이걸 열면
    app.run(debug=True)              #함수들이 다 돌아가는것을 원치 않기때문에. 지금은 다른파일에 붙여서 실행하는건 아니라 필요는 없지만은 다르사람이
                           # 이 파일을 열어서 실행할때는 이 if절이 반드시 들어가있어야 한다. 



#0.0.0.0해야지만 외부에서도 테스트 할 수 있다.
# port는     


