from faker import Faker

fake = Faker()
print('Init Faker')

from faker.providers import BaseProvider

class GeoHashProvider(BaseProvider):
	def geohash(self):
		# if i remember right, a geohash was lat-long formated: xx.xx,yy.yy
		lat1 = self.random_int(1,32)
		lat2 = self.random_digit()
		lat3 = self.random_digit()
		
		lng1 = self.random_int(1,32)
		lng2 = self.random_digit()
		lng3 = self.random_digit()
		
		
		geo_lat = '%d.%d%d' % (lat1, lat2, lat3)
		geo_lng = '%d.%d%d' % (lng1, lng2, lng3)
		
		return '%s,%s' % (geo_lat, geo_lng)
		

class YakkerIDProvider(BaseProvider):
	def yakkerID(self):
		return self.random_int(1, 10000)
	
class EventProvider(BaseProvider):
	_events = {'getMessages': 0.5, 'getComments': 0.1, 'getFeed' : 0.1, 'getHot' : 0.1, 'postComment' : 0.1, 
							'postMessage': 0.2}
							
	def event(self):
		return self.random_element(self._events)
		
class YakarmaProvider(BaseProvider):
	def yakarma(self):
		return self.random_int(100, 100000)
	