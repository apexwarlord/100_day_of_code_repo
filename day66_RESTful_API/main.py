from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import random
from flask import jsonify
import sys

API_KEY = 'TopSecretAPIKey'

ErrorLocNF = {"not found": "Sorry, there is no cafe in that location"}

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


def make_dict(cafe):
    columns = cafe.__table__.columns
    return {column.name: getattr(cafe, column.name) for column in columns}


@app.route("/")
def _index():
    return render_template("index.html")


@app.route("/all")
def _all():
    all_cafes = Cafe.query.all()
    all_cafes_dict = [make_dict(cafe) for cafe in all_cafes]

    return jsonify(all_cafes=all_cafes_dict)


@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def _update_price(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    new_price = request.args.get("new_price")
    if not cafe:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    elif not new_price:
        return jsonify(error={"Missing parameter": "No new_price parameter provided"}), 400
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200


@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def _report_closed(cafe_id):
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    api_key = request.args.get("api_key")
    if api_key != API_KEY:
        return jsonify(error={"unauthorized": "You did not provide the access API Key"}), 403
    elif not cafe:
        return jsonify(error={"Cafe not found": "You did not provide a cafe id that is in our database"}), 404
    else:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully removed the cafe"})


@app.route("/add", methods=["POST"])
def _add():
    try:
        new_cafe = Cafe(
            name=request.form['name'],
            location=request.form['location'],
            seats=request.form['seats'],
            img_url=request.form['img_url'],
            map_url=request.form['map_url'],
            coffee_price=request.form['coffee_price'],
            has_wifi=request.form['has_wifi'] == 'true',
            has_toilet=request.form['has_toilet'] == 'true',
            has_sockets=request.form['has_sockets'] == 'true',
            can_take_calls=request.form['can_take_calls'] == 'true',
        )
    except KeyError as e:
        return jsonify(error={"Bad Request": f"{e} Some or all fields were incorrect or missing."})
    else:
        with app.app_context():
            db.session.add(new_cafe)
            db.session.commit()
        return jsonify(response={"success": f"Successfully added the new cafe."})


@app.route("/random")
def _random():
    all_cafes = Cafe.query.all()
    random_cafe = random.choice(all_cafes)

    return jsonify(random_cafe=make_dict(random_cafe))


@app.route("/search")
def _search():
    if request.method == 'GET':
        params = request.args.to_dict()  # returns a dictionary object with attribute: search pair
        if params.get('location'):
            params["location"] = params["location"].title()
        if params.get('name'):
            params["name"] = params["name"].title()
        search_results = Cafe.query.filter_by(**params).all()
        # location = request.args.get("loc").title()
        # search_results = Cafe.query.filter_by(location=location).all()
        if search_results:
            all_cafes_dict = [make_dict(cafe) for cafe in search_results]
            return jsonify(results=all_cafes_dict)
        else:
            return jsonify(error=ErrorLocNF)
    else:
        return "invalid request"


## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
