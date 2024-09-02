#Monkey Patched lol
import httpx

original_client = httpx.Client

def patched_client(*args, **kwargs):
    kwargs.pop('proxy', None)
    return original_client(*args, **kwargs)

httpx.Client = patched_client

from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
from dotenv import load_dotenv
import os
from random import randint


#Configuration
load_dotenv(dotenv_path="secret.env")
USERNAME = os.getenv('User_Name')
EMAIL = os.getenv('Email')
PASSWORD = os.getenv('Password')

#Params
MINIMUM_TWEETS = 10
QUERY = "$ETH"
FILTER = "Latest"

# Initialize Client
client = Client()


#WE RUN LINES 37 TO 43 ONLY ONCE
#Login to twitter the first time then use cookies
# client.login(
#         auth_info_1=USERNAME,
#         auth_info_2=EMAIL,
#         password=PASSWORD
#     )
#Save Cookies   
# client.save_cookies('cookies.json')

#Load JSON data
client.load_cookies('cookies.json')

tweet_count = 0
tweets = None

while tweet_count < MINIMUM_TWEETS:
    if tweets is None:
        #Get Tweets
        print(f'{datetime.now()} - Getting tweets...')
        tweets = client.search_tweet(QUERY, product=FILTER)
    else:
        print(f'{datetime.now()} - Getting next tweets...')
        tweets = tweets.next()
    if not tweets:
        print(f'{datetime.now()} - No more tweets found')
    for tweet in tweets:
        tweet_count += 1
        tweet_data = [tweet_count, tweet.user.name, tweet.text, tweet.created_at, tweet.retweet_count, tweet.favorite_count, tweet.reply_count]
        print(tweet_data)
    print(f'{datetime.now()} - Done! Got {tweet_count} tweets found')    