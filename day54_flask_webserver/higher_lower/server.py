from flask import Flask, redirect
from random import randint

correct_num = randint(1, 9)

app = Flask(__name__)


@app.route('/')
def homepage():
    return ('<h1>Guess a number between 1 and 9</h1>'
            '<img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWVibjdyNWhkYTA5MzAxcXdvZXI5bWwydXlwMjJsNzlnbTZncnc0YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l378khQxt68syiWJy/giphy.gif" />')


@app.route('/play_again', methods=["GET"])
def play_again_redirect():
    global correct_num
    correct_num = randint(1, 9)
    return redirect("/", code=302)


@app.route('/<int:n>')
def guess(n):
    print(n)
    print(correct_num)
    if n < correct_num:
        return ('<h2 style="color:red;">TOO LOW!</h2>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGo0M2hveW4zazFqYXNwdmR1N2gycWZ3OWlwdTVwNWQ3bGowODhpMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bgWypySe8IW4AnmJIU/giphy.gif" />')
    elif n > correct_num:
        return ('<h2 style="color:purple;">TOO HIGH!</h2>'
                '<img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2c0andoMWtuNm41aXVtbTZqMmJscGJ1bndlaDNtazNya25nNXRoMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/H6K49nnOGvBAc/giphy.gif" />')
    else:
        return ('<h2 style="color:green;">YOU FOUND ME!</h2>'
                '<img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExODJienAzMW5mYWxvN2xtMHFsbGdwdjMwZWtpeHdzMmJlNGhla3Z1dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pwUXY9irbzveOL4vr6/giphy.gif" />'
                '<br/><a href="/play_again">PLAY AGAIN!</a>')


if __name__ == "__main__":
    app.run(debug=True)
