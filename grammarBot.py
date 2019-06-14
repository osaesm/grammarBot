import os
import praw

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

username = os.getenv('USER_NAME')
password = os.getenv('PASSWORD')

reddit = praw.Reddit(client_id='g-w3B3ZvdFg6hA',
                     client_secret='RuZ6TZWQYEyhFUpHIKe2ZSazsps',
                     username=username,
                     user_agent='grammar bot by /u/boxerboy40',
                     password=password)

for comment in reddit.subreddit('all').comments(limit=25):
    print('would of' in str.lower(comment.body))
