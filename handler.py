# Imports
import socketio
from keys import *

streamlabs = socketio.Client()

streamlabs.connect(f"https://sockets.streamlabs.com?token={socketToken}")

streamlabs.wait()

@streamlabs.event
def message(eventData)
    if eventData.for == null and eventData.type == "donation"
        print(f"{eventData.name} donated {eventData.formattedAmount}")
    else if eventData.for == "twitch_account"
        if eventData.type == "follow"
            print(f"{eventData.name} followed")
        else if eventData.type == "subscription"
            print(f"{eventData.name} subscribed")
        else if eventData.type == "bits"
            print(f"{eventData.name} sent {eventData.amount} bits")