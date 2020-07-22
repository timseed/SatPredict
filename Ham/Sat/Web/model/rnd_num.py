from controllers import app
from controllers import socketio
from random import random
from flask import render_template

from time import sleep
from threading import Thread, Event

thread_stop_event = Event()
gbl_thread = Thread()


def randomNumberGenerator():
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    # infinite loop of magical random numbers
    print("Making random numbers")
    while not thread_stop_event.isSet():
        number = round(random() * 10, 3)
        print(number)
        socketio.emit("newnumber", {"number": number}, namespace="/test")
        socketio.sleep(5)


def delayed_start():
    print("in delayed start")
    sleep(1)
    randomNumberGenerator()


@app.route("/")
def index():
    print("Index hit")
    # only by sending this page first will the client be connected to the socketio instance
    return render_template("index.html")


@socketio.on("connect", namespace="/test")
def test_connect():
    global gbl_thread
    # need visibility of the global thread object
    print("Client connected")

    # Start the random number generator thread only if the thread has not been started before.
    if not gbl_thread.isAlive():
        print("Starting Thread from connect")
        gbl_thread = socketio.start_background_task(randomNumberGenerator)


@socketio.on("disconnect", namespace="/test")
def test_disconnect():
    print("Client disconnected")