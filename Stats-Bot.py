import tweepy
import os
import logging

from flask import Flask, render_template

app = Flask(__name__)

from bots.config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_followers_details(api):

    logger.info("Retrieving my followers ...")
    return tweepy.Cursor(api.followers).items()


@app.route("/")
def index():

    logger.info("Started logging ...")
    api = create_api()
    followers = get_followers_details(api)

    return render_template("index.html", followers=followers)


if __name__ == "__main__":
    pass
