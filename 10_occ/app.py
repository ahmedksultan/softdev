#   Lauren Pehlivanian, Ahmed Sultan
#   SoftDev1 pd9
#   K10 -- Jinja Tuning
#   2019-09-24

from flask import Flask, render_template
import occuPicker as randOcc
from collections import OrderedDict
import jinja2

app = Flask(__name__)

@app.route("/occupyflaskst")
def occ():
    return render_template(
        "template.html",
        title="Team Chuck Schumer",
        header="Lauren and Ahmed, pd. 9",
        random_occupation=randOcc.main(),
        tblHeading1="Occupation",
        tblHeading2="Percent",
        dict=randOcc.dictGenerate("occupations.csv")
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
