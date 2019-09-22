# Imports
import socketio
from keys import *

streamlabs = socketio.Client()

streamlabs.connect(f"https://sockets.streamlabs.com?token={socketToken}")

sio.wait()