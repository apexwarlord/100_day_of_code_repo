from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, validators
from wtforms.validators import DataRequired, Regexp
import csv
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class AddCafeForm(FlaskForm):
    name = StringField('Cafe Name', validators=[DataRequired()], render_kw={"maxlength": 36})
    location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), Regexp(regex='^https://.*', flags=re.IGNORECASE, message="Only links starting with 'https://' are allowed")])
    open = StringField('Opening Time e.g.: 8AM', validators=[DataRequired()], render_kw={"maxlength": 12})
    close = StringField('Closing Time e.g.: 6PM', validators=[DataRequired()], render_kw={"maxlength": 12})
    coffee_ratings = [('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'), ('☕☕☕☕', '☕☕☕☕')]
    coffee = SelectField(u'Coffee Rating', choices=coffee_ratings, validators=[DataRequired()])
    wifi_ratings = [('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪')]
    wifi = SelectField('Wifi Rating', choices=wifi_ratings, validators=[DataRequired()])
    socket_ratings = [('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌')]
    socket = SelectField('Power Socket Availability', choices=socket_ratings, validators=[DataRequired()])

    submit = SubmitField('Add')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = AddCafeForm()
    if form.validate_on_submit():
        data = [form.data["name"], form.data["location"], form.data["open"], form.data["close"], form.data["coffee"], form.data["wifi"], form.data["socket"]]
        with open('cafe-data.csv', 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',',)
            writer.writerow(data)
        return redirect('/cafes')

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)