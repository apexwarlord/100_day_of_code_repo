from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        pw = request.form['pw']
        print(name, pw)
        return render_template('login.html', name=name, pw=pw)
    else:
        redirect('/')


if __name__ == "__main__":
    app.run(debug=True)