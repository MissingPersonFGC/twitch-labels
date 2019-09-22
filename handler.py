# Imports
import socketio
from keys import *

socketToken = 

sio = socketio.Client(f"https://sockets.streamlabs.com?token={socketToken}")

sio.connect()