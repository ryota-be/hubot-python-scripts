import os

from scripts.hubot_script import *

class Develop(HubotScript):
    
    @respond('message')
    def message(self, message, matches):
        return str(message)

	@respond('matches')
	def match(self,message,matches):
		return str(matches)
