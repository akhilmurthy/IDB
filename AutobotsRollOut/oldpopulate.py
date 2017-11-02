import urllib.request
import json
import ssl
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Hero, TopPlayer, Achievement, Event, Skin, Item
import psycopg2
import os

from html.parser import HTMLParser


baseurl = 'https://overwatch-api.net/api/v1'
context = ssl._create_unverified_context()

db.reflect()
db.drop_all()
db.create_all()

def scrapeHeroes():
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
		role_name = data['role']['name']
		abilities_list = data['abilities']


		b = False

		name_str = ''
		ulti = ''
		for i in abilities_list:
			if i['is_ultimate']:
				ulti = i['name']
			else:
				if not b:
					name_str += i['name'] 
					b = True
				else:
					name_str += ', '
					name_str += i['name']

		# print(str(Hero_id) + " " + name + "\n" + description + "\n"+ name_str + "\n"+ ulti ) 
		hero = Hero(Hero_id, name, description, role_name, name_str, ulti)
		db.session.add(hero)
		db.session.commit()



		#Need to insert these into the Database

def scrapeAchievements():

	for h in range(1, 74):
		tempurl = baseurl + '/achievement/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		try:
			thejson = urllib.request.urlopen(req, context=context)
		except:
			pass
		else:
			data_bytes = thejson.read().decode('utf-8')
			data = json.loads(data_bytes)

			achievement_id = data['id']
			name = data['name']
			description = data['description']
			reward = data['reward']['name']
			reward_type = data['reward']['type']['name']
			reward_quality = data['reward']['quality']['name']

			f_key = None
			if(data['hero'] is not None):
				f_key = data['hero']['id']


		# 

	#all the url, info to create each json
		# print(str(achievement_id) + " "+ name + "\n"+ description)
			achieve = Achievement(achievement_id, name, description, reward, reward_type, reward_quality,f_key)
			db.session.add(achieve)
			db.session.commit()

def scrapeEvents():

	for h in range(1, 4):
		tempurl = baseurl + '/event/' + str(h)
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		
		name = data['name']
		start = data['start_date']
		end = data['end_date']

		event = Event(h, name, start, end)
		db.session.add(event)
		db.session.commit()

	#all the url, info to create each json

def scrapeSkinsItems():

	for h in range(1, 100):
		tempurl = baseurl + '/reward/' + str(h)

		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		reward_type = data['type']['name']
		hero_id = None
		if data['hero'] is not None:
			hero_id = data['hero']['id']

		event_id = None
		if data['event'] is not None:
			event_id = data['event']['id']

		if  reward_type == 'skin':
			skin_name = data['name']
			if data ['cost'] != None:
				skin_cost = data['cost']['value'] + " credits"
			else:
				skin_cost = None
			quality = data['quality']['name']

			skin = Skins(h, skin_name, skin_cost, quality, hero_id, event_id)
			db.session.add(skin)
			db.session.commit()
		else:
			if reward_type == 'spray' or reward_type == 'player icon':
				item = reward_type
				item_name = data['name']
				item_type = data['type']['name']
				item = Items(h, item_name, item_type, event_id)
				db.session.add(item)
				db.session.commit()

battletags = []

class MyHTMLParser(HTMLParser):
	#add to battletags
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "a":
           # Check the list of defined attributes.
           profileurl = ""

           for name, value in attrs:
               # If href is defined, print it.
               #print("-"+name)
               if name == "href":
                   if "us" in value:
                       profileurl = value
                       print("---" + profileurl)
                       #cut up isolate profileurl
                       battletags.append(profileurl)
                       #popTopPlayers()


def scrapeTopPlayers():
	leaderboardurl = "https://masteroverwatch.com/leaderboards/pc/us/mode/ranked/category/skillrating"
	req = urllib.request.Request(leaderboardurl, headers={'User-Agent': 'Mozilla/5.0'})
	theimage = urllib.request.urlopen(req, context=context)
	parser = MyHTMLParser()
	parser.feed(str(theimage.read()))

def popTopPlayers():
	#battletags = ['SPREE-2984', 'HaventMetYou-2451', 'Hydration-1570', 'zombs-1642', 'Seraphic-21298', 'Jchuk99-1390', 'SumAwsomeKid-1356', 'YLLES-3238', 'SKRRSKRR-1878', 'NotE-1996']
	#top 10 players to start with
	for h in range(0, 10):
		tempurl = "https://owapi.net/api/v3/u/" + battletags[h] + "/blob"
		req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
		thejson = urllib.request.urlopen(req, context=context)
		data_bytes = thejson.read().decode('utf-8')
		data = json.loads(data_bytes)

		name = battletags[h]
		win_rate = data['us']['stats']['competitive']['overall_stats']['win_rate']
		tier = data['us']['stats']['competitive']['overall_stats']['tier']
		level = data['us']['stats']['competitive']['overall_stats']['level']
		skill_rank = data['us']['stats']['competitive']['overall_stats']['comprank']

		topPlayer = TopPlayer(h, name, win_rate, tier, level, skill_rank )

		db.session.add(topPlayer)
		db.session.commit()
		# print(win_rate)
		# print(tier)
		# print(level)
		# print(skill_rank)
		# print("--------")
	    # parse json here
	    #print(thejson.read())
		time.sleep(5)

	#all the url, info to create each json


def main():
	#scrapeHeroes()
	#scrapeAchievements()
	#scrapeEvents()
	#scrapeSkinsItems()
	scrapeTopPlayers()

if __name__ == "__main__": main()