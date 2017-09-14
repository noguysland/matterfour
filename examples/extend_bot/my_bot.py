
from matterfour.mattbot import MattBot
from matterfour.mattermost import MattermostAdapter
import settings		# local settings

class MyBot(MattBot):

	def __init__(self):
		self._adapter = MattermostAdapter(
			settings.MM_URL, settings.BOT_LOGIN_ACC, settings.BOT_PASSWORD,
			settings.BOT_TEAMS, settings.SSL_VERIFY)

if __name__ == "__main__":
	MyBot().run()