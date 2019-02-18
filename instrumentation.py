import os
import analytics

key = os.environ['KEY']
analytics.write_key = key


class SegmentImpl():

    def __init__(self, userInfo):
        self.userInfo = userInfo
        analytics.identify(userInfo.userid,{
            'name': userInfo.name,
            'email': userInfo.email
        })

    def send(self, trackingEvent):
        analytics.track(self.userInfo.userid, 'event', {
            'name': trackingEvent[0],
            'eventName': trackingEvent[1],
            'geohash': trackingEvent[2],
            'yakkerID': trackingEvent[3],
            'yakarma': trackingEvent[4]
            })

        



