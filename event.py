from datetime import datetime

class Event:
    def __init__(self, event_data = None):
        # if there is no event data passed, set empty string as event data
        if event_data == None:
            event_data = ""

        self.Event_Data = event_data
        self.EventDateTimeUtc = datetime.utcnow().strftime("%d-%m-%Y %H:%M:%S.%f")