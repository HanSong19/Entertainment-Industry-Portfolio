from flask import Flask, render_template, request
import os
app = Flask(__name__)
#요청 들어오면 돌려보내줄 route를 다 만들어 놓는다#
@app.route("/fileform") #.com/ 이후(거의 첫번째 페이지에)에서 뭔가 요구하면은 다음을 보여 주겠다
def fileform(): #보통 별다른 요청 없이 들어오는 페이지를 index.jsp등으로쓰기 때문에 그냥 index라고 이름을 주로 잡는다, 함수 이름이 중복되면 안됨
    return render_template('upload.html') #이것을 그러면 response에 실어서 사용자(client)에게 보내준다


@app.route("/fileUpload/", methods = ['POST']) #method 안적엇으니까 default 로 get이다
def fileUpload():          #http://127.0.0.1:5000/login/?name=han
    f= request.files['file']
    print(type(f))
    dirname = os.path.dirname(__file__) + "/uploads/" +f.filename #밑에 터미널에 나는 PS E:\201906송한별\work\github\pythonprojects> 까지만 되잇어서 flask 다음 uploads해야한다
    print(dirname)
    f.save(dirname)
    return 'upload 성공'  #만약에 여기서 다른 페이지로 넘어 가고 싶으면 return  render_template한다음에 그페이지로 넘어가면 된다

  



if __name__ == '__main__': #원래 함수는 호출하기전에 실행이 안되는데 run은 이것들을 다 실행 해버리는 것이다. 다른파일에서 이걸 열면
    app.run(debug=True)              #함수들이 다 돌아가는것을 원치 않기때문에. 지금은 다른파일에 붙여서 실행하는건 아니라 필요는 없지만은 다르사람이
                           # 이 파일을 열어서 실행할때는 이 if절이 반드시 들어가있어야 한다. 



#0.0.0.0해야지만 외부에서도 테스트 할 수 있다.
# port는     


