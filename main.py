from twikit import Client, TooManyRequests
import time
from datetime import datetime
import csv
import asyncio
from dotenv import load_dotenv
import os
from configparser import ConfigParser
from random import randint

load_dotenv(dotenv_path="secret.env")
USERNAME = os.getenv('Username')
EMAIL = os.getenv('Email')
PASSWORD = os.getenv('Password')

# Initialize Client
client = Client('en-US')

async def main():
    await client.login(
        auth_info_1=USERNAME,
        auth_info_2=EMAIL,
        password=PASSWORD
    )

asyncio.run(main())

