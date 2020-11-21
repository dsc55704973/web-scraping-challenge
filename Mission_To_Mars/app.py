# create a scraper -> return a dictionary with results
# 2 end points
#   1. home page - retrieve (render template with data from mongoDB)
#   2. scrape - call the scrape function -> return that dictionary

from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import scrape_mars

app=Flask(__name__)

app.config['MONGO_URI']='mongodb://localhost:27017/mars_app/'
mongo=PyMongo(app)



@app.route('/')
def index():
    results=mongo.db.mars.find_one()
    # print(results)
    print(type(results))
    # return jsonify(results)
    print(results.first())
    return results.first()
    return render_template('index.html', mars_data=results.test)

@app.route('/scrape')
def scrape():
    mongo.db.mars.update({}, test_data, upsert=True)
    return redirect('/')
    return "updated"

if __name__=='__main__':
    app.run()



