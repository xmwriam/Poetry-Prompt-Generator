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
    headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}
    r = requests.get('https://api.reddit.com/r/WritingPrompts/', headers=headers)
    L =  r.json()
    num=len(L['data']['children'])
    ind=random.randint(3,num-1)
    return L['data']['children'][ind]['data']['title'][4::]

#app.run(debug=True)