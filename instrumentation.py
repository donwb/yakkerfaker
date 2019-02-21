import os
import analytics
import mparticle

key = os.environ['KEY']
analytics.write_key = key

class MParticleImpl():
    # batch = mparticle.Batch()

    def __init__(self, userInfo):
        self.userInfo = userInfo
        self.batch = mparticle.Batch()
        self.batch.environment = 'development'

        configuration = mparticle.Configuration()
        configuration.api_key = os.environ['MP_KEY']
        configuration.api_secret = os.environ['MP_SECRET']


        configuration.debug = True #enable logging of HTTP traffic
        self.api_instance = mparticle.EventsApi(configuration)

        mp_identity = mparticle.UserIdentities()
        mp_identity.customerid = userInfo.userid
        mp_identity.email = userInfo.email
        mp_identity.other = userInfo.name

        self.batch.user_itentities = mp_identity


    def send(self, trackingEvent):
        app_event = mparticle.AppEvent('Example', 'navigation')
        # app_event.timestamp_unixtime_ms = example_timestamp
        self.batch.events = [app_event]

        self.api_instance.upload_events(self.batch)

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

        



