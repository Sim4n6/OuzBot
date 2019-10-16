import tweepy
import os
import logging

from flask import Flask, render_template

app = Flask(__name__)

from bots.config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_friends_not_followers(api):

    fnf = []
    logger.info("Retrieving my friends not followers ...")
    followers = tweepy.Cursor(api.followers).items()
    for following in tweepy.Cursor(api.friends).items():
        if following not in followers: 
            fnf.append(following)
    return fnf


@app.route("/")
def index():

    logger.info("Started logging ...")
    api = create_api()
    users = get_friends_not_followers(api)

    return render_template("index.html", fnf=users)


if __name__ == "__main__":
    pass
