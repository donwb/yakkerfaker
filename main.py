from faker import Faker
from yakker import *
from instrumentation import *
from videostart import *
from datetime import datetime
from time import sleep
import csv
import threading
import os
import collections

writeOutFile = os.environ['WRITE_OUT_FILE'] == 'true'
iterations = int(os.environ['ITERATIONS'])
runForever = iterations == -1

totalCounter = 0

def init():
	users = setupUsers()

	threads = []

	for u in users:
		si = SegmentImpl(u)
		mp = MParticleImpl(u)

		threads.append(
			threading.Thread(target=start, args=(si, mp,))
		)
		threads[-1].start()

	for t in threads:
		t.join()
		
def test():
    print('testing new code....')

    page_fake = Faker()
    page_fake.add_provider(AppNameProvider)
    page_fake.add_provider(IDProvider)
    page_fake.add_provider(CampaignProvider)

    makePageEvent(page_fake)



def start(si, mp):
	fake = Faker()

	page_fake = Faker()

	print("starting.....")
	
	fake.add_provider(EventProvider)
	fake.add_provider(GeoHashProvider)
	fake.add_provider(YakkerIDProvider)
	fake.add_provider(YakarmaProvider)
	page_fake.add_provider(AppNameProvider)
	page_fake.add_provider(IDProvider)
	page_fake.add_provider(CampaignProvider)


	with open('yakkerevents.csv', 'w') as myfile:
		wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)		
		
		# doing a while so it can run for infinity
		c = 0
		while True:
			yd = makeYakkerData(si.userInfo.userid, fake.event(), fake.geohash(),
										 fake.yakkerID(), fake.yakarma())
			yd_mp = makeYakkerData('donwb', fake.event(), fake.geohash(),
										 fake.yakkerID(), fake.yakarma())
			if writeOutFile:
				wr.writerow(yd)
			
			si.send(yd)
			mp.send(yd_mp)

			print(".", end="", flush=True)
			
			# lot of code for a counter, but here we are
			global totalCounter
			lock = threading.Lock()			
			with lock:
				totalCounter += 1
			
			sleep(0.05)

			# this checks to see if there's an end defined, if not run until
			# the cows come home
			c+=1
			if not runForever:
				if c >= iterations:
					print(str(totalCounter) + ' records generated')
					break
				
	
	print()
	print("complete! ", si.userInfo.name)

def makeYakkerData(user, event, geohash, yakkerID, yakarma):
	now = datetime.utcnow()
	
	yakkerList = [user, event, geohash, yakkerID, yakarma, str(now)]
	
	return yakkerList

def makePageEvent(page_faker):
    app_name = page_faker.appname()
    bu = 'cnn'
    code_version = 'v1'
    full_url = 'tbd'
    gu_id = page_faker.randomID()
    krux_id = page_faker.randomID()
    highlander_id = page_faker.randomID()
    adobe_user_id = page_faker.randomID()
    campaign = page_faker.campaign()

    page_event = [app_name, bu, code_version, full_url, gu_id, krux_id, highlander_id, adobe_user_id, campaign]


    print(page_event)


	

def setupUsers():
	User = collections.namedtuple("User", "userid name email")

	Don = User(userid="donwb", name="Don Browning", email="don.browning@gmail.com")
	Brian = User(userid="boneil", name="Brian Oneil", email="brian.oneil@turner.com")
	Matthew = User(userid="mdrooker", name="Matthew Drooker", email="matthew.drooker@turner.com")
	Tony = User(userid="thoensen", name="Tony Thoensen", email="tony.thoensen@turner.com")

	return [Don, Brian, Matthew, Tony]

if __name__ == '__main__':
	# init()
    test()
	
	


