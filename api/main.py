from flask import Flask
from flask import render_template
import requests
import random
app = Flask(__name__)

@app.route("/")
def lauunch():
    return render_template("yayy.html")

@app.route("/generator")
def gen():
    return render_template("poetry.html")

@app.route("/prompt")
def prompt():
    user_agent_list =['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',]
    headers = {'User-Agent': user_agent_list[random.randint(0,2)]} 
    r = requests.get('https://api.reddit.com/r/WritingPrompts/', headers=headers)
    L =  r.json()
    num=len(L['data']['children'])
    ind=random.randint(3,num-1)
    return L['data']['children'][ind]['data']['title'][4::]
