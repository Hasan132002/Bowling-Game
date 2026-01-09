FALLBACK = {
    "STRIKE2": "STRIKE1",
    "STRIKE3": "STRIKE1",
    "DOUBLE2": "DOUBLE1",
    "DOUBLE3": "DOUBLE1",
    "TURKEY2": "TURKEY1",
    "TURKEY3": "TURKEY1",
    "HIGHGAM2": "HIGHGAM1",
    "HIGHGAM3": "HIGHGAM1",
}

def map_event(event):
    return FALLBACK.get(event, event)
