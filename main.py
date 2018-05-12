from faker import Faker
from yakker import *
from datetime import datetime
from time import sleep
import csv

def start():
	fake = Faker()

	print("starting.....")
	
	fake.add_provider(EventProvider)
	fake.add_provider(GeoHashProvider)
	fake.add_provider(YakkerIDProvider)
	fake.add_provider(YakarmaProvider)
	
	with open('yakkerevents.csv', 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)		
		for _ in range(1000):
			yd = makeYakkerData(fake.event(), fake.geohash(),
										 fake.yakkerID(), fake.yakarma())

			wr.writerow(yd)
			sleep(0.05)
	
	print("complete!")

def makeYakkerData(event, geohash, yakkerID, yakarma):
	now = datetime.utcnow()
	
	yakkerList = [event, geohash, yakkerID, yakarma, str(now)]
	
	return yakkerList


if __name__ == '__main__':
	start()

