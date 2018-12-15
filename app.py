#################################
# Flask app for mission to mars #
#################################

# import libraries
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# Setup the MongoDB
client = pymongo.MongoClient()
db = client['mars_db']
# Get collections
dict_news = db['dic_news']
featured_images = db['featured_img']
weather = db['mars_weather']
# hemisphere = db['hemisphere_img_urls']

# create route that renders index.html template
@app.route("/")
def home():
    dic_news = dict_news.find()
    featured_img = featured_images.find()
    mars_weather = weather.find()
    # full_hemisphere_dict = db.collection_hemisphere.find()
    return render_template("index.html", dic_news = dic_news, featured_img = featured_img, mars_weather = mars_weather)
    # full_hemisphere_dict = full_hemisphere_dict

@app.route("/scrape")
def scrape():
    dict_news.remove()
    dic_news = scrape_mars.mars_news()
    dict_news.insert_one(dic_news)

    featured_images.remove()
    featured_img = scrape_mars.featured_image()
    featured_images.insert_one(featured_img)

    weather.remove()
    mars_weather = scrape_mars.mars_weather_fun()
    weather.insert_one(mars_weather)

    # hemisphere.remove()
    # hemisphere_img_urls = scrape_mars.mars_hemispheres()
    # hemisphere.insert_one(hemisphere_img_urls)

    print('----------------')
    print(dic_news)
    print('----------------')
    print(featured_img)
    print('----------------')
    print(mars_weather)
    print('----------------')
    # print(hemisphere_img_urls)
    
    return redirect("http://127.0.0.1:5000")

if __name__ == "__main__":
    app.run(debug=True)