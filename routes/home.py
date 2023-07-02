from flask import render_template
from flask import Blueprint

blueprint = Blueprint("home", __name__)

@blueprint.route("/")
def home():
    return render_template("index.html")