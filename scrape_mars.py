###########################
# Functions for the Flask #
###########################

# Library
from bs4 import BeautifulSoup as bs
from splinter import Browser
import os
import pandas as pd
import time

# Open browser function
browser = Browser('chrome', headless=True)

# Mars News
def mars_news():
    browser.visit("https://mars.nasa.gov/news/")
    parsed = bs(browser.html,'html.parser')
    # Retrieve a list of the headings
    article_headings = []
    for article_heading in parsed.find_all('div',class_="content_title"):
        article_headings.append(article_heading.find('a').text)
    # Retrieve a list of the article teaser texts
    article_bodies = []
    for article_body in parsed.find_all('div',class_="article_teaser_body"):
        article_bodies.append(article_body.text)
    # Most recent news is first
    firsthead = article_headings[0]
    firsttease = article_bodies[0]
    dic_news = {"title": firsthead, "teaser": firsttease}
    return dic_news

# JPL Mars Space Images - Featured Image
def featured_image():
    browser.visit("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
    parsed = bs(browser.html,'html.parser')
    # Retrieving all images
    images = []
    for image in parsed.find_all('div',class_="img"):
        images.append(image.find('img').get('src'))
    # Finding the most recent image
    # The maximum resolution is (640x350)
    latest_image = images[0]
    featured_image_url = "https://www.jpl.nasa.gov" + latest_image
    featured_img = {"featured_img": featured_image_url}
    return featured_img

# Mars Weather
def mars_weather_fun():
    browser.visit("https://twitter.com/marswxreport?lang=en")
    parsed = bs(browser.html,'html.parser')
    # Retrieving all tweets
    tweets = []
    for tweet in parsed.find_all('p',class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"):
        tweets.append(tweet.text)
    # Finding the most recent tweet
    mars_weather = {"mars_weather": tweets[0]}
    return mars_weather

# Mars Facts
def mars_facts():
    facts_df = pd.read_html("http://space-facts.com/mars/")[0]
    facts_df.rename_axis({0:"Variable", 1:"Value"},axis=1, inplace=True)
    # Saving the DF as an HTML table string
    facts_df_html = facts_df.to_html("facts_df.html", index=False)
    facts_df_dic = {"facts_table": facts_df_html}
    return facts_df_dic

# Mars Hemispheres
# Website was under maintenance
# def mars_hemispheres():
#    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")
#    parsed = bs(browser.html,'html.parser')
#    # Fetch hemisphere image titles
#    hemisphere_titles = []
#    for title in parsed.find_all('div',class_="description"):
#        hemisphere_titles.append(title.find('h3').text)
#    # Getting the titles as a link format so we can get the full size images
#    hemispheres = ["cerberus", "schiaparelli", "syrtis_major", "valles_marineris"]
#    # Fetch hemisphere image URLs
#    hemisphere_images = []
#    for name in hemispheres:
#        hemisphere_images.append("https://astrogeology.usgs.gov/download/Mars/Viking/" + name + "_enhanced.tiff")
#    # Saved as a dictionary. Not sure what was meant by appending a list so we have one dictionary per hemisphere? 
#    # So I made two dictionaries, one with title and url as the key, and one as the title for the key
#    hemisphere_image_urls_key = {"title":hemisphere_titles,"img_url":hemisphere_images}
#    hemisphere_image_urls = dict(zip(hemisphere_titles, hemisphere_images))
#    return hemisphere_image_urls

