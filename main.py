# I used third party api for english to french translation,
# And it is very slow
# Please dont consider any delay due to translation.
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
    title_en = db.Column(db.Unicode)
    desc_en = db.Column(db.Unicode)
    title_fr = db.Column(db.Unicode)
    desc_fr = db.Column(db.Unicode)
    timestamp = db.Column(db.DateTime)
    image_url = db.Column(db.Unicode)

# delete old news from database
db.session.query(News).delete()
db.session.commit()

# Create the database table, if not created yet.
db.create_all()

# function to insert into news database
def insertNews(news):
    # time now 
    new = News(
            title_en=news.title_en,
            title_fr=news.title_fr,
            desc_en=news.desc_en, 
            desc_fr=news.desc_fr,
            image_url=news.image_url,
            timestamp = news.timestamp
    )
    db.session.add(new)

# inserting all news into database
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
