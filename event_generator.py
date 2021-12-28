import time
import event as e
import event_publisher

class EventGenerator():
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher

    def generate_test_events(self):       
        counter = 1
        while counter <= 1000:            
            test_evt = e.Event("test_event_data_{0}".format(counter))
            self.event_publisher.publish_event(test_evt)
            counter += 1
            time.sleep(5)