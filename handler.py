# Imports
import socketio
from keys import *

streamlabs = socketio.Client()

streamlabs.connect(f"https://sockets.streamlabs.com?token={socketToken}")

streamlabs.wait()

@streamlabs.event
def message(eventData)
    print('something happened')
    print(eventData)