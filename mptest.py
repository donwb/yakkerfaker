import mparticle
import os

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
