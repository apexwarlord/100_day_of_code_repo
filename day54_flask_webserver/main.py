from flask import Flask

app = Flask(__name__)


def style_b(fxn):
    def wrapper():
        return "<b>" + fxn() + "</b>"

    return wrapper


def style_em(fxn):
    def wrapper():
        return "<em>" + fxn() + "</em>"

    return wrapper


def style_u(fxn):
    def wrapper():
        return "<u>" + fxn() + "</u>"

    return wrapper


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/bye')
@style_b
@style_em
@style_u
def hello_world():
    return 'Goodbye, World!'


if __name__ == "__main__":
    app.run(debug=True)