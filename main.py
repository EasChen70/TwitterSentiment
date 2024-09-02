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

#Get Tweets
tweets = client.search_tweet(QUERY, product = "Top")