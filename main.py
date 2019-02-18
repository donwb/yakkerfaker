from faker import Faker
from yakker import *
from instrumentation import *
from datetime import datetime
from time import sleep
import csv
import threading
import os

writeOutFile = os.environ['WRITE_OUT_FILE'] == 'true'
iterations = int(os.environ['ITERATIONS'])
runForever = iterations == -1

totalCounter = 0

def init():
	

	users = ['donwb', 'mdrooker', 'boneil', 'bsolomon']
	#users = ['donwb']
	threads = []

	for u in users:
		si = SegmentImpl(u)
		threads.append(
			threading.Thread(target=start, args=(si,))
		)
		threads[-1].start()

	for t in threads:
		t.join()
		
	

def start(si):
	fake = Faker()

	print("starting.....")
	
	fake.add_provider(EventProvider)
	fake.add_provider(GeoHashProvider)
	fake.add_provider(YakkerIDProvider)
	fake.add_provider(YakarmaProvider)

	with open('yakkerevents.csv', 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)		
		
		# doing a while so it can run for infinity
		c = 0
		while True:
			yd = makeYakkerData(si.user, fake.event(), fake.geohash(),
										 fake.yakkerID(), fake.yakarma())
			if writeOutFile:
				wr.writerow(yd)
			
			si.send(yd)
			print(".", end="", flush=True)
			
			# lot of code for a counter, but here we are
			global totalCounter
			lock = threading.Lock()			
			with lock:
				totalCounter += 1
			
			sleep(0.05)

			c+=1
			if not runForever:
				if c >= iterations:
					print(str(totalCounter) + ' records generated')
					break
				
	
	print()
	print("complete! ", si.user)

def makeYakkerData(user, event, geohash, yakkerID, yakarma):
	now = datetime.utcnow()
	
	yakkerList = [user, event, geohash, yakkerID, yakarma, str(now)]
	
	return yakkerList


if __name__ == '__main__':
	init()
	
	


