from Ham.Sat.Web.controllers import socketio
from Ham.Sat.Web.controllers.app import app

"""
Project to demonstration Async IO in flask/Web
"""
if __name__ == "__main__":
    from Ham.Sat.Web.model.rnd_num import *
    from Ham.Sat.Web.model.hello import *

    socketio.run(app, host="127.0.0.1", port=5000)

