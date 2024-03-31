from flask import Flask
from flask import render_template
import random
import praw
import os
app = Flask(__name__)

@app.route("/")
def lauunch():
    return render_template("yayy.html")

@app.route("/generator")
def gen():
    return render_template("poetry.html")

@app.route("/prompt")
def prompt():
    reddit = praw.Reddit(
    client_id=os.environ['clientID'],
    client_secret=os.environ['clientSecret'],
    user_agent=os.environ['userAgent'],
)
    prompts=[]
    for submission in reddit.subreddit("WritingPrompts").hot(limit=10):
        prompts.append(submission.title)
    print(prompts)
    num=len(prompts)
    ind=random.randint(0,num-1)
    return prompts[ind][4::]