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
MINIMUM_TWEETS = 99
QUERY = "$ETH"
FILTER = "Latest"

# Get Tweets function
def get_tweets(tweets):
    if tweets is None:
        print(f'{datetime.now()} - Getting tweets...')
        tweets = client.search_tweet(QUERY, product=FILTER)
    else:
        #add delays to simulate human behavior
        wait_time = randint(6,13)
        print(f'{datetime.now()} - Getting next tweets after {wait_time} seconds...')
        time.sleep(wait_time)
        tweets = tweets.next()
    return tweets

# Create a csv file
with open('tweets.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Tweet_Count', 'Username', 'Text', 'Created At', 'Retweets', 'Favorites', 'Replies'])


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
    try:
        tweets = get_tweets(tweets)
    except TooManyRequests as e:
        rate_limit_reset = datetime.fromtimestamp(e.rate_limit_reset)
        print(f'{datetime.now} - Rate limit reached. Waiting until {rate_limit_reset}')
        wait_time = rate_limit_reset - datetime.now()
        time.sleep(wait_time.total_seconds())
        continue
    if not tweets:
        print(f'{datetime.now()} - No more tweets found')
        break
    for tweet in tweets:
        tweet_count += 1
        tweet_data = [tweet_count, tweet.user.name, tweet.text, tweet.created_at, tweet.retweet_count, tweet.favorite_count, tweet.reply_count]
        with open('tweets.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(tweet_data)
    print(f'{datetime.now} - Got {tweet_count} tweets')        

print(f'{datetime.now()} - Done! Got {tweet_count} tweets found')    