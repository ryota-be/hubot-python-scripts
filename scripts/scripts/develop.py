# -*- coding:utf-8 -*-
import os
from scripts.hubot_script import *
import urllib2
import json
import datetime
class Develop(HubotScript):
	keymember = []
	@respond('message( )?.*')
	def message(self, message, matches):
		return str(message)#{u'message': u'message', u'type': u'respond', u'room': u'bot_dev'}

	@respond('matches()?.*')
	def match(self,message,matches):
		return str(matches)

	@respond('house()?.*')
	def houseInfo(self,message,matches):
		response = urllib2.urlopen('https://script.google.com/macros/s/AKfycbz53s9DehPewIBvUlx-iNyZzEeWB_be707gP8i98r-FoBb3G-7w/exec')
		data = []
		data = json.loads(response.read())
		today = datetime.date.today()
		day_key = str(today.year).zfill(4)+'/'+str(today.month).zfill(2)+'/'+str(today.day).zfill(2)
		s = day_key + " attendance\n"
		alert = 'Fill this sheet immediately\nhttps://docs.google.com/spreadsheets/d/1KJ18JLS6JbZT6RgzfjF7-i3y6S8tpkSlcgDAAb4Rtyk/edit#gid=745264158\n'
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

	@respond('gomi()?.*')
	def garbage(self,message,matches):
		return '古紙:水\n容器包装・プラスチック:水\n燃やすゴミ:火金\n金属・陶器・ガラスゴミ:第２・第４土'

	@respond('keydef [^ ]+ [^ ]+ [^ ]+ [^ ]+')
	def keydef(self,message,matches):
		Develop.keymember = []
		for i in range(1,5):
			Develop.keymember.append(message.split(' ')[i])
		return 'ok'

	@respond('key')
	def keyshow(self,message,matches):
		return str(Develop.keymember)

	@respond('key [^ ]+ [^ ]+')
	def keyChange(self,message,matches):
		Develop.keymember[Develop.keymember.index(message.split(' ')[1])] = message.split(' ')[2]
		return 'ok'

	@respond('blog()?.*')
	def blogShow(self,message,matches):
		dic = [("Mon:","滝川"),("Tue:","火曜日も滝川"),("Wed:","水曜日の滝川"),("Thu:","木曜日の人"),("Fri:","金曜日の滝川"),("Sat:","土曜日てみー"),("Sun:","にちようびてみー")]
		today = datetime.date.today()
		i = today.weekday()
		ret = ""
		for j in range(0,6):
			if i > 6:
				i = 0
			ret += dic[i][0] + dic[i][1] + '\n'
			i += 1
		return ret

