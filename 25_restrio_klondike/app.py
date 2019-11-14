# Klondike -- Nahi Khan, Lauren Pehlivanian and Ahmed Sultan
# SoftDev1 pd 9
# K25 -- Getting more REST
# 2019-11-13

from flask import Flask, render_template
import urllib
import random
import json

app = Flask(__name__)

# countries, currency exchange, & studio ghibli

@app.route("/")
def main():
    # accessing countries API
    u = urllib.request.urlopen("https://restcountries.eu/rest/v2")
    response = u.read()
    data = json.loads(response)

    # picking random country from API response
    rand_num = random.randint(0, 249)
    ctry_name = data[rand_num]['name']
    ctry_capital = data[rand_num]['capital']
    ctry_flag = data[rand_num]['flag']
    ctry_currency = data[rand_num]['currencies'][0]['name']
    ctry_languages = []
    for i in data[rand_num]['languages']:
        ctry_languages.append(i['name'])

    return render_template("index.html", name=ctry_name, flag=ctry_flag, capital=ctry_capital, currency=ctry_currency, languages=ctry_languages)

if __name__ == "__main__":
    app.debug = True
    app.run()
