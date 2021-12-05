# imports
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from scrape import getNewsList
from flask_restless import APIManager

# configuring db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'
db = SQLAlchemy(app)

# Declaring database schema
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Unicode)
    description = db.Column(db.Unicode)
    imageUrl = db.Column(db.Unicode)

# delete old news from database
db.session.query(News).delete()
db.session.commit()

# Create the database tables.
db.create_all()

# insert into news
def insertNews(news):
    new = News(title=news.title, description=news.description, imageUrl=news.imageUrl)
    db.session.add(new)

for news in getNewsList():
    insertNews(news)

# committing to db
db.session.commit()

# Create the Flask-Restless API manager.
manager = APIManager(app, flask_sqlalchemy_db=db)

# creating API with endpoint /api/news
manager.create_api(News, methods=['GET'])

# start the flask loop
app.run(debug=True)
