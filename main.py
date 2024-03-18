from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def lauunch():
    return render_template("yayy.html")

@app.route("/generator")
def gen():
    return render_template("poetry.html")


app.run(debug=True)