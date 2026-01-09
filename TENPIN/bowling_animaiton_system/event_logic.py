def process_event(event):
    valid = ["STRIKE", "SPARE", "DOUBLE", "TURKEY"]
    if event in valid:
        return event
    return None
