from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
from Ham.Sat.Web.controllers.app import app
from Ham.Sat.Web.controllers.socketio import socketio
