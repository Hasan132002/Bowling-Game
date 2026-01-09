'''import time

def listen_for_event():
    """
    Demo event generator.
    Baad me yahan serial / OCR add hoga.
    """
    events = ["STRIKE", "SPARE", "DOUBLE", "TURKEY"]

    for e in events:
        time.sleep(5)
        yield e
'''

import serial

ser = serial.Serial("COM3", 9600)

def listen_for_event():
    while True:
        line = ser.readline().decode(errors="ignore")
        if "STRIKE" in line:
            yield "STRIKE"
