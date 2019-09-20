#   Ahmed Sultan
#   SoftDev1 pd9
#   demo -- create a flask app with 3 routes
#   2019-09-18w

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    print(__name__)
    return __name__


@app.route("/zoolander")
def hello_obama():
    print('Serving /zoolander...')
    return "what is this? a center for ants?"


@app.route("/bueller")
def hello_bueller():
    print("Serving /bueller...")
    return "bueller... bueller... bueller..."


@app.route("/borat")
def hello_joe():
    print("wa wa we wa!")
    return "jagshemash!"


if __name__ == "__main__":
    app.debug = True
    app.run()
