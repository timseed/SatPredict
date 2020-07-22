# Start with a basic flask app webpage.
from flask import Flask
import os

__author__ = "Tim Seed"
template_dir = os.path.abspath("./templates")
print(f"setting template_dir to {template_dir}")
app = Flask(__name__, template_folder=template_dir)
app.config["SECRET_KEY"] = "secret!"
app.config["DEBUG"] = True
app.config["ENV"] = "Development"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["FLASK_DEBUG"] = True
app.config["EXPLAIN_TEMPLATE_LOADING"] = True