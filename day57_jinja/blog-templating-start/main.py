from flask import Flask, render_template, redirect
import requests


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog = response.json()
    return render_template("index.html", blog=blog)

@app.route('/post/<int:post_id>')
def render_post(post_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blog = response.json()

    post_data = None
    for post in blog:
        if post['id'] == post_id:
            post_data = post
            break

    if post_data is None:
        return redirect("/")

    return render_template("post.html", post_data=post_data)


if __name__ == "__main__":
    app.run(debug=True)
