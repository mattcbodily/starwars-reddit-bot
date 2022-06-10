import os
from os.path import join, dirname
from dotenv import load_dotenv
import praw

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

reddit = praw.Reddit(
  user_agent="<HermitLukeBot 1.0 https://github.com/mattcbodily/starwars-reddit-bot>",
  client_id=os.environ.get("CLIENT_ID"),
  client_secret=os.environ.get("CLIENT_SECRET"),
  username="Hermit_Luke_Bot",
  password=os.environ.get("PASSWORD")
)