import os

from scripts.hubot_script import *

class Develop(HubotScript):
	@respond('message( )?.*')
	def message(self, message, matches):
		return str(message)#{u'message': u'message', u'type': u'respond', u'room': u'bot_dev'}

	@respond('matches()?.*')
	def match(self,message,matches):
		return str(matches)
