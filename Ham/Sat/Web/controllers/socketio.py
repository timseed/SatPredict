# Start with a basic flask app webpage.
from flask_socketio import SocketIO
from Ham.Sat.Web.controllers import app

# turn the flask app into a socketio app
socketio = SocketIO(app, async_mode=None, logger=True, engineio_logger=True)