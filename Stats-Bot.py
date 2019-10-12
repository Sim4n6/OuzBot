import tweepy
import os
import logging

from bots.config import create_api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_followers(api):
    logger.info("Retrieving my followers ...")
    followers = tweepy.Cursor(api.followers).items()
    for i, follower in enumerate(followers):
        logger.info(f"My follower {i} name :  {follower.name}")

    return followers


def get_user_detail(api, follower):

    logger.info("get user details needed.")
    user = api.get_user(follower)
    logger.info(
        f"User name: {user.screen_name} - {user.followers_count} - is following ? {user.following}"
    )

    return user


if __name__ == "__main__":

    logger.info("Started logging ...")
    api = create_api()
    followers = get_followers(api)
    for follower in followers:
        user = get_user_detail(api, follower)
