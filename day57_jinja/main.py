from datetime import datetime
from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)


@app.route('/')
def homepage():
    # get the current year
    year = datetime.now().year
    return render_template('index.html', year=year)


@app.route('/guess', methods=["GET"])
def basic_redirect():
    return redirect("/", code=302)


@app.route('/guess/<name>')
def name_guess(name):
    response_gender = requests.get(f"https://api.genderize.io?name={name.lower()}")
    response_age = requests.get(f"https://api.agify.io?name={name.lower()}")
    title_name = name.title()
    gender = response_gender.json()["gender"]
    age = response_age.json()["age"]

    if gender is None:
        gender = "male or female"

    if age is None:
        age = "Some number of"

    return render_template('guess.html', age=age, name=title_name, gender=gender)


@app.route('/blog')
def render_blog():
    response_blog = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response_blog.json()
    return render_template('blog.html', posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
