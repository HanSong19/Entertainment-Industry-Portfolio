from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def hello_admin():
    return render_template('movie_bootstrap_copy.html')


if __name__ == "__main__":
    app.run(debug = True)
