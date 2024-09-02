from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
import asyncio
from dotenv import load_dotenv
import os
from configparser import ConfigParser
from random import randint

MINIMUM_TWEET = 10
QUERY = 'chatgpt'


load_dotenv(dotenv_path="secret.env")
USERNAME = os.getenv('Username')
EMAIL = os.getenv('Email')
PASSWORD = os.getenv('Password')

# Initialize Client
client = Client('en-US')
    #Login
async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )
    #Use Cookies   
    await client.save_cookies('cookies.json')

    client.load_cookies('cookies.json')

    tweet_count = 0

    tweets = await client.search_tweet(QUERY, product='Top')

    for tweet in tweets:
        tweet_count += 1
        tweet_data = [tweet_count, tweet.user.name, tweet.text, tweet.created_at, tweet.retweet_count, tweet.favorite_count]
        print(vars(tweet))
        break

# Run the main function
asyncio.run(main())