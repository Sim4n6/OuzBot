import tweepy
import os
import logging

from flask import Flask, render_template, url_for

app = Flask(__name__)

from bots.config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_followers_details(api):

    followers = []

    logger.info("Retrieving my followers ...")
    for i, follower in enumerate(tweepy.Cursor(api.followers).items()):
        logger.info(f"Follower {i} name: {follower.name}")
        followers.append(get_user_detail(api, i, follower.id))

    return followers


def get_user_detail(api, i, follower):

    logger.info("get user details needed ...")
    user = api.get_user(follower)
    logger.info(
        f"Username {i}: {user.screen_name} - {user.name} - \n\t is following ? {user.following} - {user.id} - {user.description} - \n\tfollowers count:{user.followers_count} - Statuses count: {user.statuses_count}"
    )

    return user


@app.route("/")
def hello_world():

    logger.info("Started logging ...")
    api = create_api()
    followers = get_followers_details(api)

    return render_template("index.html", followers=followers)


if __name__ == "__main__":
    pass
