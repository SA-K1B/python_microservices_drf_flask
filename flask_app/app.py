from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/flask_db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_db'
migrate = Migrate(app,db)

@dataclass
class Meal(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    area = db.Column(db.String(50))
    liked = db.Column(db.Boolean)
@app.route('/',methods = ['POST'])
def home():
    data = request.get_json()
    # print(data['name'])
    # print(type(data))
    meal = Meal(id= data['id'], name= data['name'], category= data['category'], area= data['area'], liked= data['liked'])
    # print(meal)
    db.session.add(meal)
    db.session.commit()
    get_meal = Meal.query.get(1)
    # print(get_meal.name)
    return jsonify(
        {
          "name": get_meal.name
        }
    )
if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')
