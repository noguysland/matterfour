
from matterfour import settings
from matterfour.mattermost import MattermostAdapter

class MattBot(object):

	def __init__(self):
		self._adapter = MattermostAdapter(
			settings.MM_URL, settings.BOT_LOGIN_ACC, settings.BOT_PASSWORD,
			settings.BOT_TEAMS, settings.SSL_VERIFY)

	def run(self):
		pass

	def _keep_active(self):
		pass