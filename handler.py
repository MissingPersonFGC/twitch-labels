# Imports
import socketio
from keys import *

streamlabs = socketio.Client()

# Connect to the streamlabs socket API
streamlabs.connect(f"https://sockets.streamlabs.com?token={socketToken}")

# Grab event
@streamlabs.event
def message(eventData)
    if eventData.for == null and eventData.type == "donation"
        print(f"{eventData.message.name} donated {eventData.formattedAmount}")

        # Load the text file and write
        text = open("donation.txt", "w")
        text.write(f"{eventData.message.name} ({eventData.formattedAmount})")
        text.close()
    else if eventData.for == "twitch_account"
        if eventData.type == "follow"
            print(f"{eventData.message.name} followed")

            # Load the text file and write
            text = open("twitch_follow.txt", "w")
            text.write(eventData.message.name)
            text.close()
        else if eventData.type == "subscription"
            print(f"{eventData.message.name} subscribed on Twitch")

            # Load the text file and write
            text = open("twitch_sub.txt", "w")
            text.write(eventData.message.name)
            text.close()
        else if eventData.type == "bits"
            print(f"{eventData.message.name} sent {eventData.message.amount} bits")

            # Format bits into a dollar amount
            formattedBits = f"${eventData.message.amount / 100}"

            # Load the text file and write
            text = open("donation.txt", "w")
            text.write(f"{eventData.message.name} ({formattedBits})")
            text.close()
    else if eventData.for == "youtube_account"
        if eventData.type == "follow"
            print(f"{eventData.message.name} subscribed on Youtube")

            # Load the text file and write
            text = open("youtube_follow.txt", "w")
            text.write(eventData.message.name)
            text.close()
        else if eventData.type == "subscription"
            print(f"{eventData.message.name} sponsored")

            # Load the text file and write
            text = open("youtube_subscription.txt", "w")
            text.write(eventData.message.name)
            text.close()
        else if eventData.type == "superchat"
            print(f"{eventData.message.name} donated {eventData.message.displayString} on Youtube")

            # Load the text file and write
            text = open("donation.txt", "w")
            text.write(eventData.message.displayString)
            text.close()
    else if eventData.for == "mixer_account"
        if eventData.type == "follow"
            print(f"{eventData.message.name} followed on Mixer")

            # Load the text file and write
            text = open("mixer_follow.txt", "w")
            text.write(eventData.message.name)
            text.close()
        else if eventData.type == "subscription"
            print(f"{eventData.message.name} subscribed on Mixer")

            # Load the text file and write
            text = open("mixer_subscription.txt", "w")
            text.write(eventData.message.name)
            text.close()

# Leave the connection open
streamlabs.wait()