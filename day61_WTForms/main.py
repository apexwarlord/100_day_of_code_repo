from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap

CREDENTIALS = ("admin@email.com", "12345678")


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app


app = create_app()
app.config['SECRET_KEY'] = 'ZANDERZ'


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={"maxlength": 30})
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 30)], render_kw={"maxlength": 30})
    submit = SubmitField('Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if CREDENTIALS == (form.email.data.strip(), form.password.data):
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)