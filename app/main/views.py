from flask import render_template
from . import main
from manage import app

@app.route("/")
def index():

    return render_template("index.html")