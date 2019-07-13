from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello_admin():
    return render_template('main.html')
'''
@app.route("/guest/<guest>")
def hello_guest(guest):
    return redirect("/")
'''

if __name__ == "__main__":
    app.run(debug = True)
