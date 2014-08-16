import os

from scripts.hubot_script import *
import urllib2
import json
import datetime
class Develop(HubotScript):
	@respond('message( )?.*')
	def message(self, message, matches):
		return str(message)#{u'message': u'message', u'type': u'respond', u'room': u'bot_dev'}

	@respond('matches()?.*')
	def match(self,message,matches):
		return str(matches)

	@respond('house()?.*')
	def houseInfo(self,message,matches):
		response = urllib2.urlopen('https://script.google.com/macros/s/AKfycbww_pq15yfa6reDG0HIKfAcZssf61Vrq9DNJuVk87XD9_QNICI/exec')
		data = []
		data = json.loads(response.read())
		diff = (datetime.date.today() - datetime.date(2014,8,7)).days
		s = "Today's attendance\n"
		for row in data[4:]:
			s += row.values()[0] + ':'
			s += row.values()[diff] + '\n'
		return s
