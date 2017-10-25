# from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
# from models import db, Heroes, TopPlayers, Achievements, Events, Skins, Items
import urllib.request
import json
import ssl
import time

baseurl = 'https://overwatch-api.net/api/v1'
context = ssl._create_unverified_context()

def scrapeHero():
#24 heroes
	for h in range(1, 25):
		tempurl = baseurl + '/hero/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		skins = data['rewards']
		hero = data['name']
		print (hero + "= [",end = "")
		for x in skins:
			if x['type']['name'] == 'skin':
				print ('"' + x['name']+ '"' +  ", ",end = "")
		print("]")


def main():
	scrapeHero()
	# scrapeAchievements()
	#scrapeEvents()
	#scrapeSkinsItems()
	#scrapeTopPlayers()

if __name__ == "__main__": main()