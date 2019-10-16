import tweepy
import os
import logging

from flask import Flask, render_template

app = Flask(__name__)

from bots.config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_friends_not_followers(api):

    logger.info("Retrieving my friends not followers ...")
    return tweepy.Cursor(api.friends).items() - tweepy.Cursor(api.followers).items()


@app.route("/")
def index():

    logger.info("Started logging ...")
    api = create_api()
    users = get_friends_not_followers(api)

    return render_template("index.html", followers=users)


if __name__ == "__main__":
    pass
