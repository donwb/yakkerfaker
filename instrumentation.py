import os
import analytics
import mparticle

key = os.environ['KEY']
analytics.write_key = key

class MParticleImpl():
    def __init__(self, userInfo):
        self.userInfo = userInfo
        # how do I set mParticle user info?

    def send(self, trackingEvent):
        # Factor all this out since it works different from Segment
        batch = mparticle.Batch()
        batch.environment = 'development'


        configuration = mparticle.Configuration()
        configuration.api_key = os.environ['MP_KEY']
        configuration.api_secret = os.environ['MP_SECRET']


        configuration.debug = True #enable logging of HTTP traffic
        api_instance = mparticle.EventsApi(configuration)

        app_event = mparticle.AppEvent('Example', 'navigation')
        # app_event.timestamp_unixtime_ms = example_timestamp
        batch.events = [app_event]

        api_instance.upload_events(batch)

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

        



