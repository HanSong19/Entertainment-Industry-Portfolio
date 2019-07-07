from flask import Flask, render_template, request
app = Flask(__name__)
#요청 들어오면 돌려보내줄 route를 다 만들어 놓는다#
@app.route("/") 
def index(): 
    return render_template("form_input.html")


@app.route("/login/", methods = ['POST']) 
def login_post():          
    result = request.form
    print(type(result))
    return render_template('form_result.html', result=result)

if __name__ == '__main__': 
    app.run(debug=True)            
                           



#0.0.0.0해야지만 외부에서도 테스트 할 수 있다.
# port는     


