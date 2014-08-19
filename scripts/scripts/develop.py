# -*- coding:utf-8 -*-
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
		today = datetime.date.today()
		day_key = str(today.year).zfill(4)+'/'+str(today.month).zfill(2)+'/'+str(today.day).zfill(2)
		s = "Today's attendance\n"
		alert = 'Fill this sheet immediately\nhttps://docs.google.com/spreadsheets/d/1KJ18JLS6JbZT6RgzfjF7-i3y6S8tpkSlcgDAAb4Rtyk/edit#gid=0\n'
		for key in data[0].keys():
			if day_key in key:
				day_key = key
		for row in data[4:]:
			s += row.values()[0].split('@')[0] + ':'
			if row[day_key]:
				s += row[day_key]
			else:
				alert += '@'+row.values()[0].split('@')[1]+': '
			s += '\n'
		s += alert
		return s
