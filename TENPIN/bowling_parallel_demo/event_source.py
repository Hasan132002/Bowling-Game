import time
import random

# All bowling events
EVENT_SEQUENCE = [
    "OPENFRM1",
    "SPARE1",
    "STRIKE1",
    "DOUBLE1",
    "STRIKE2",
    "DOUBLE2",
    "TURKEY1",
    "STRIKE3",
    "TURKEY2",
    "TURKEY3",
    "FOUL",
    "FENCE",
    "CLEANGAM",
    "HIGHGAM1",
    "HIGHGAM2",
    "HIGHGAM3",
    "PERFGAME"
]

def listen_events():
    print("📡 Demo Event Engine Started (Original-style)")

    while True:
        for event in EVENT_SEQUENCE:
            print("📡 Event:", event)
            yield event
            time.sleep(4)   # natural bowling delay
