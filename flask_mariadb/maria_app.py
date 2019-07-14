from flask import Flask, render_template, request, redirect
import db

app = Flask(__name__)

db.create_table()
#요청 들어오면 돌려보내줄 route를 다 만들어 놓는다#
@app.route("/") 
def index(): 
    return render_template("main.html")


@app.route("/insert", methods = ['POST']) 
def login_post():     
    user = request.form.to_dict()     
    db.insert_info(list(user.values()))
    print(list(user.values()))
    users=db.all_users()
    return render_template('list.html', users=users)  #list.html 에 users라는 것을 넘길 것이다

@app.route('/list')
def list_user():
    users=db.all_users()
    return render_template('list.html', users=users)

@app.route('/content/<userid>')
def content_user(userid):
    user=db.one_user(userid)
    return render_template('content.html', user = user)

@app.route('/delete/<userid>')
def delete_user(userid):
    db.delete_user(userid)
    return redirect('/list')

@app.route('/updateform/<userid>')
def updateform(userid):
    user = db.one_user(userid)
    return render_template ('updateform.html', user = user)

@app.route('/update', methods = ['POST'])
def update_user():
    user = request.form.to_dict()
    print(user)
    db.update_user(user)
    return redirect('/list')

if __name__ == '__main__': 
    app.run(debug=True)            
                           



#0.0.0.0해야지만 외부에서도 테스트 할 수 있다.
# port는     


