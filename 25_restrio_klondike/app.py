# Klondike -- Nahi Khan, Lauren Pehlivanian and Ahmed Sultan
# SoftDev1 pd 9
# K25 -- Getting more REST
# 2019-11-13

from flask import Flask, render_template
import urllib
import json

app = Flask(__name__)

# Ahmed Sultan
# SoftDev 1 pd 9
# K24 -- A RESTful Journey Skyward
# 2019-11-12

app = Flask(__name__)


@app.route("/")
def main():
    u = urllib.request.urlopen(
        "https://api.nasa.gov/planetary/apod?api_key=I9chRrUh43ayV1eRZa53qAmYznCGebkcoAtye5kP")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", header=data['title'], picture=data['url'], info=data['explanation'])


if __name__ == "__main__":
    app.debug = True
    app.run()