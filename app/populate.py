import urllib.request
import json
import ssl
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from models import db, Heroes, TopPlayers, Achievements, Events, Skins, Items


baseurl = 'https://overwatch-api.net/api/v1'
context = ssl._create_unverified_context()

def getHeroInfo():
#24 heroes
	for h in range(1, 25):
		tempurl = baseurl + '/hero/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		Hero_id = data['id']
		name = data['name']
		description = data['description']

		abilities_list = data['abilties']

		b = false

		name_str = ''
		ulti = ''
		for i in abilties_list:
			if i['is_ultimate']:
				ulti = i['name']
			else:
				if not b:
					name_str += i['name'] 
					b = true
				else
					name_str += ', '
					name_str += i['name'] 




		#Need to insert these into the Database
		







#def getPlay  erInfo():

	#all the url, info to create each json

def getAchievementInfo():

	for h in range(1, 75):
		tempurl = baseurl + '/achievement/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		name = data['name']
		description = data['description']

	#all the url, info to create each json

def getEventsInfo():

		for h in range(1, 4):
			tempurl = baseurl + '/event/' + str(h)
			req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
			thejson = urllib.request.urlopen(req, context=context)
			data_bytes = thejson.read().decode('utf-8')
			data = json.loads(data_bytes)

			name = data['name']
			start = data['start_date']
			end = data['end_date']

	#all the url, info to create each json

def getSkinsInfo():

	for h in range(1, 1887):
			tempurl = baseurl + '/reward/' + str(h)
			req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
			thejson = urllib.request.urlopen(req, context=context)
			data_bytes = thejson.read().decode('utf-8')
			data = json.loads(data_bytes)

			reward_type = data['type']['name']
			if  reward_type == 'skin':
				print(data['name'])


	#all the url, info to create each json

#def getItemsInfo():

	#all the url, info to create each json

def main():
	getSkinsInfo()

if __name__ == "__main__": main()