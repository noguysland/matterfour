
class MattermostAdapter(object):

	def __init__(self, mm_url, bot_acc, bot_passwd, bot_teams=[], sl_verify=False):
		self.teams = bot_teams
		self.account = bot_acc
		self.password = bot_passwd