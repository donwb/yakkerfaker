import os
import analytics

key = os.environ['KEY']
analytics.write_key = key


class SegmentImpl():

    def __init__(self, userid):
        self.user = userid
        analytics.identify(userid,{
            'name': 'Don Browning',
            'email': 'don.browning@gmail.com'
        })

    def send(self, trackingEvent):
        analytics.track(self.user, 'event', {
            'name': trackingEvent[0],
            'geohash': trackingEvent[1],
            'yakkerID': trackingEvent[2],
            'yakarma': trackingEvent[3]
            })

        



