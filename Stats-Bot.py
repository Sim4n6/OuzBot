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
    logger.info("Retrieving my friends not followers (fnf)...")
    followers = tweepy.Cursor(api.followers).items()
    for friend in tweepy.Cursor(api.friends).items():
        if friend not in followers: 
            fnf.append(friend)
    return fnf


@app.route("/")
def index():

    logger.info("Started logging ...")
    api = create_api()
    fnf = get_friends_not_followers(api)

    return render_template("index.html", fnf=fnf, len_fnf=len(fnf))


if __name__ == "__main__":
    pass
