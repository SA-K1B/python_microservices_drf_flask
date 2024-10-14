from flask import Flask,jsonify,request,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests
from flask_migrate import Migrate
from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.getenv('db_user')}:{os.getenv('db_password')}@localhost:5432/{os.getenv('db_name')}"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgresql-flask/flask_db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_db'
migrate = Migrate(app,db)

@dataclass
class Meal(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    area = db.Column(db.String(50))
    image = db.Column(db.String(200))
    # liked = db.Column(db.Boolean)
@app.route('/searched',methods = ['GET'])
def index():
    return render_template('searchedMeal.html')
@app.route('/api/searched-meal',methods = ['GET'])
def home():
    # data = request.get_json()
    # print(data['name'])
    # print(type(data))
    # meal = Meal(id= data['id'], name= data['name'], category= data['category'], area= data['area'], liked= data['liked'])
    # # print(meal)
    # db.session.add(meal)
    # db.session.commit()
    get_meal = Meal.query.all()
    # print(get_meal.name)
    meals=[]
    for i in get_meal:
        meals.append({
            "id": i.id,
            "name": i.name,
            "category": i.category,
            "area": i.area,
            "image": i.image
        })
        
    return jsonify(
        {
          "meals": meals
        }
    )
if __name__ == '__main__':
    app.run(debug=True,host = '0.0.0.0')
