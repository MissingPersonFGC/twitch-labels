# Imports
import socketio
from keys import *

streamlabs = socketio.Client()

streamlabs.connect(f"https://sockets.streamlabs.com?token={socketToken}")

@streamlabs.event
def message(eventData)
    if eventData.for == null and eventData.type == "donation"
        print(f"{eventData.name} donated {eventData.formattedAmount}")
        text = open("donation.txt", "w")
        text.write(f"{eventData.name} ({eventData.formattedAmount})")
        text.close()
    else if eventData.for == "twitch_account"
        if eventData.type == "follow"
            print(f"{eventData.name} followed")
            text = open("twitch_follow.txt", "w")
            text.write(eventData.name)
            text.close()
        else if eventData.type == "subscription"
            print(f"{eventData.name} subscribed")
            text = open("twitch_sub.txt", "w")
            text.write(eventData.name)
            text.close()
        else if eventData.type == "bits"
            print(f"{eventData.name} sent {eventData.amount} bits")
            formattedBits = f"${eventData.amount / 100}"
            text = open("donation.txt", "w")
            text.write(f"{eventData.name} ({formattedBits})")
            text.close()
            
streamlabs.wait()