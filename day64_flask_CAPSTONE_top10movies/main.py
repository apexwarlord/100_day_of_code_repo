from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''TMDB CREDENTIALS'''
API_KEY = 'a6ea2ab9224359904f14d7aea25622ae'
SEARCH_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
DETAILS_ENDPOINT = "https://api.themoviedb.org/3/movie/"
POSTER_PATH = "https://image.tmdb.org/t/p/original"
# parameter: query (string required)
SEARCH_PARAMS = {
    "query": "dummy",
    "include_adult": False,
    "language": "en-US",
}
HEADERS = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNmVhMmFiOTIyNDM1OTkwNGYxNGQ3YWVhMjU2MjJhZSIsInN1YiI6IjY1YmMyYWFlMWZkMzZmMDE3ZDczNTAxNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nk-HJNSXmYvSqYoH24h2iTRvggcWNz2ZXK_SICcgnoY"
}

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
# Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLES
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(320), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, unique=False, nullable=True)
    review = db.Column(db.String(320), nullable=True)
    img_url = db.Column(db.String(320), nullable=False)

    def __repr__(self):
        return f'<Movie {self.ranking} - {self.title}>'


'''Build tables'''


# with app.app_context():
#     db.create_all()


# function to add movie
def make_movie(title, year, description, img_url):
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        rating=None,
        ranking=None,
        review=None,
        img_url=img_url
    )
    return new_movie


# WTF Edit and Add forms
class EditForm(FlaskForm):
    rating = StringField('New Rating', validators=[DataRequired()], render_kw={"maxlength": 4})
    review = StringField('Review', validators=[DataRequired()], render_kw={"maxlength": 320})
    submit = SubmitField('Update movie details')


class AddForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={"maxlength": 80})
    submit = SubmitField('Add movie')


@app.route("/")
def home():
    with app.app_context():
        ranked_movies = Movie.query.order_by(Movie.rating).all()
        for i, movie in enumerate(ranked_movies):
            movie.ranking = len(ranked_movies) - i

        # Query all rows and order them by the 'ranking' column
        # all_movies = Movie.query.order_by(Movie.ranking.desc()).all()
        return render_template("index.html", all_movies=ranked_movies)


@app.route("/edit", methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    with app.app_context():
        movie = Movie.query.filter_by(id=movie_id).first()
        if form.validate_on_submit():
            try:
                movie.rating, movie.review = round(float(form.rating.data.strip()), 1), form.review.data.strip()
                db.session.commit()
            except ValueError:
                return render_template("edit.html", movie=movie, form=form,
                                       error_msg="Submit a rating between 0 and 10.0")
            else:
                return redirect('/')
    return render_template("edit.html", movie=movie, form=form, error_msg=None)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    with app.app_context():
        movie = Movie.query.filter_by(id=movie_id).first()
        db.session.delete(movie)
        db.session.commit()
    return redirect("/")


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        SEARCH_PARAMS["query"] = form.title.data.strip()
        results = requests.get(url=SEARCH_ENDPOINT, params=SEARCH_PARAMS, headers=HEADERS).json()["results"]
        if results:
            return render_template("select.html", results=results)
        else:
            return render_template("add.html", form=form, error_msg="No results found for that search")

    return render_template("add.html", form=form, error_msg=None)


@app.route("/find", methods=['GET'])
def find_movie():
    movie_id = request.args.get("id")
    results = requests.get(url=DETAILS_ENDPOINT + movie_id, headers=HEADERS).json()
    print(results)
    title = results["title"]
    year = int(results["release_date"][:4])
    description = results["overview"]
    img_url = POSTER_PATH + results["poster_path"]
    new_movie = make_movie(title, year, description, img_url)
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()

    added_movie = Movie.query.filter_by(title=title).first()
    return redirect(url_for('edit', id=added_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
