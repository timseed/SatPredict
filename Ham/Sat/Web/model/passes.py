from Ham.Sat.Web.controllers import app
from Ham.Sat.Web.controllers import socketio
from Ham.Sat.Passes import Passes
from flask import render_template
from time import sleep
from threading import Thread, Event
from dataclasses import asdict
passes_thread_stop_event = Event()
passes_gbl_thread = Thread()

def getpasses():
    """
    Generate a random number every 1 second and emit to a socketio instance (broadcast)
    Ideally to be run in a separate thread?
    """
    my_tracker = Passes()
    app.logger.debug("In getpasses")
    # infinite loop of magical random numbers
    while not passes_thread_stop_event.isSet():
        pss = my_tracker.predict(days=2.0,max_passes=1)
        app.logger.debug(f"we have {len(pss)} To send to web page")
        for p in pss:
            app.logger.debug(f"Sending pass {asdict(p)}")
            socketio.emit("newpass", asdict(p), namespace="/passes")
        socketio.sleep(5)



def delayed_start():
    app.logger.debug("in delayed start")
    sleep(1)
    getpasses()



@socketio.on("connect", namespace="/passes")
def test_connect():
    global passes_gbl_thread
    # need visibility of the global thread object
    app.logger.info("Client connected")

    # Start the random number generator thread only if the thread has not been started before.
    if not passes_gbl_thread.is_alive():
        app.logger.debug("Starting Thread from connect")
        gbl_thread = socketio.start_background_task(getpasses)


@socketio.on("disconnect", namespace="/passes")
def test_disconnect():
    app.logger.info("Client disconnected")

@app.route("/passes")
def render_passes():
    print("/passes hit")
    # only by sending this page first will the client be connected to the socketio instance
    return render_template("passes.html")
