from faker import Faker
from faker.providers import BaseProvider

#fake = Faker()


class AppNameProvider(BaseProvider):
	_appName = {'michonne': 0.5, 'pal': 0.3, 'cronkite' : 0.2}
							
	def appname(self):
		return self.random_element(self._appName)

class IDProvider(BaseProvider):
    def randomID(self):
        return self.random_int(100000, 9000000)

class CampaignProvider(BaseProvider):
    _campaign_name = {'camp1': 0.5, 'camp2': 0.5}

    def campaign(self):
        return self.random_element(self._campaign_name)

