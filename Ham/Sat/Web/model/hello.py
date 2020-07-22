from controllers import app
from flask import render_template


@app.route("/hello")
def hello():
    # only by sending this page first will the client be connected to the socketio instance
    return render_template("Hello.html")