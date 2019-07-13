from flask import Flask, url_for,request

app=Flask(__name__)

@app.route('/')
def index():
    pass

@app.route('/login/')
def login ():
    pass

@app.route('/user/<username>') #<>안에 있는것은 사용자가 타입하면 변수로 나오는것
def profile(username):
    pass








if __name__ == "__main__": #이파일을 다른데서 import해서 못쓰게 할때 사용한다
                          #만약에 다른데서 실행하면 if위에까지는 실행되도 밑에는 실행되지 않는다
    with app.test_request_context():
        print(url_for('index')) #url_for다음에는 함수의 이름, not the name of the route를 넣는다
        print(url_for('login'))
        print(url_for('profile', username = "hong"))
        
