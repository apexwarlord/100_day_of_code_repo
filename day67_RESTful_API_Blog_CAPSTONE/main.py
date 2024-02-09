from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import datetime
import nh3


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# # CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# # CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post", )


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()[::-1]
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = BlogPost.query.filter_by(id=index).first()
    return render_template("post.html", post=requested_post)


@app.route('/new-post', methods=['GET', 'POST'])
def make_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        data = form.data
        data.pop("submit")
        data.pop("csrf_token")
        data["body"] = nh3.clean(data["body"])
        date = datetime.today().strftime("%B %d, %Y")
        with app.app_context():
            new_post = BlogPost(**data, date=date)
            db.session.add(new_post)
            db.session.commit()
        return redirect('/')

    return render_template("make-post.html", form=form, title_line="New Post")


@app.route('/edit-post/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    edit_form = CreatePostForm(obj=post)
    if edit_form.validate_on_submit():
        with app.app_context():
            post = BlogPost.query.filter_by(id=post_id).first()
            data = edit_form.data
            post.title, post.subtitle, post.author, post.img_url, post.body = data["title"], data["subtitle"], data["author"], data["img_url"], data["body"]
            db.session.commit()
            return redirect(url_for('show_post', index=post.id))

    return render_template("make-post.html", form=edit_form, title_line="Edit Post")


@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post = BlogPost.query.filter_by(id=post_id).first()
    with app.app_context():
        post = BlogPost.query.filter_by(id=post_id).first()
        db.session.delete(post)
        db.session.commit()
        return redirect('/')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
