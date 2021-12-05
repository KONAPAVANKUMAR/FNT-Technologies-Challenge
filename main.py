# imports
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from scrape import getNewsList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)


class NewsModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(200))
    imageUrl = db.Column(db.String(200))


# cors headers
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

# delete existing data
for news in NewsModel.query.all():
    db.session.delete(news)
    db.session.commit()



# add data into newsmodel
def add_news(title, description, imageUrl):
    news = NewsModel(title=title, description=description, imageUrl=imageUrl)
    db.session.add(news)
    db.session.commit()

# create table
# db.create_all()

add_news('test', 'test','test')
# create api with flask restless
from flask_restless import APIManager
manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(NewsModel, methods=['GET', 'POST', 'DELETE', 'PUT'])
app.run(debug=True)