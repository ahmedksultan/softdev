# Team Dirty Dashers - Nahi Khan and Ahmed Sultan
# SoftDev1 pd9
# K15 -- Do I Know You?
# 2019-10-02

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("login.html")


@app.route("/auth")
def auth():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    print("***DIAG: request.args['username'] ***")
    print(request.args["username"])
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template(
        "login.html"
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
