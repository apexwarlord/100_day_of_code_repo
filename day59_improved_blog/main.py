from flask import Flask, render_template, request, redirect
import requests
import smtplib
import os
from dotenv import load_dotenv

MY_EMAIL = "alexzacharias01@hotmail.com"
PERSONAL_EMAIL = "alexzacharias01@gmail.com"
PASSWORD = os.getenv("PASSWORD")

response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_data = response.json()

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', blog_data=blog_data)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        name, email, phone, message = data['name'], data['email'], data['phone'], data['message']
        if message:
            send_email(name, email, phone, message)

        return render_template('contact.html', form_submitted=True)

    return render_template('contact.html', form_submitted=False)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:num>')
def post(num):
    post_data = None
    for post in blog_data:
        if post['id'] == num:
            post_data = post
            break
    if post_data is None:
        return redirect('/')
    post_data["bg"] = '../static/assets/img/post-bg.jpg'
    return render_template('post.html', post_data=post_data)


def send_email(name, email, phone, message):
    email_message = (f"Subject:Blog Contact Message\n\nName: {name}\nEmail: {email}\n"
                     f"Phone: {phone}\nMessage: {message}").encode('utf-8')
    with smtplib.SMTP('smtp.office365.com') as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=PERSONAL_EMAIL,
            msg=email_message
        )


if __name__ == "__main__":
    app.run(debug=True)
