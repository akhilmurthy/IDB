import urllib.request
import json
import ssl
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db, Hero, TopPlayer, Achievement, Event, Skin, Item
import psycopg2
import os

import bs4
from html.parser import HTMLParser


baseurl = 'https://overwatch-api.net/api/v1'
context = ssl._create_unverified_context()
'''
db.reflect()
db.drop_all()
db.create_all()
'''
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

'''
newbattletags = []

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
                    if "profile" in value:
                        profileurl = value
                        #print("---" + profileurl)
                        #cut up isolate profileurl
                        battletag = profileurl.rsplit("/", 1)[1]
                        #print("----" + battletag)
                        newbattletags.append(battletag)                     

def scrapeTopPlayers(pages):
	for x in range(1, pages+1):
		leaderboardurl = "https://overwatchtracker.com/leaderboards/pc/global/CompetitiveRank?country=United%20States&page=" + str(x) + "&mode=1"
		req = urllib.request.Request(leaderboardurl, headers={'User-Agent': 'Mozilla/5.0'})
		theimage = urllib.request.urlopen(req, context=context)
		parser = MyHTMLParser()
		parser.feed(str(theimage.read()))
	#print(battletags)
	#print(len(battletags))
	popTopPlayers()

def popTopPlayers():
	#battletags = ['SPREE-2984', 'HaventMetYou-2451', 'Hydration-1570', 'zombs-1642', 'Seraphic-21298', 'Jchuk99-1390', 'SumAwsomeKid-1356', 'YLLES-3238', 'SKRRSKRR-1878', 'NotE-1996']
	#battletags.extend(newbattletags)
	#top 10 players to start with
	print(battletags)
	#print(newbattletags)
	for h in range(0,len(battletags)):
		repeat = True
		while repeat:
			try:
				tempurl = "https://owapi.net/api/v3/u/" + battletags[h] + "/blob"
				req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
				thejson = urllib.request.urlopen(req, context=context)
				data_bytes = thejson.read().decode('utf-8')
				data = json.loads(data_bytes)

				print("start sleep")
				time.sleep(5)
				print("end sleep")
				name = battletags[h]
				win_rate = data['us']['stats']['competitive']['overall_stats']['win_rate']
				tier = data['us']['stats']['competitive']['overall_stats']['tier']
				level = data['us']['stats']['competitive']['overall_stats']['level']
				skill_rank = data['us']['stats']['competitive']['overall_stats']['comprank']

				topPlayer = TopPlayer(h, name, win_rate, tier, level, skill_rank )
				print("-", h, name, win_rate, tier, level, skill_rank)

				
				db.session.add(topPlayer)
				db.session.commit()
				print("committed" + name)
		# print(win_rate)
		# print(tier)
		# print(level)
		# print(skill_rank)
		# print("--------")
	    # parse json here
	    #print(thejson.read())
				
			except urllib.error.HTTPError as error:
				print("caught httperror")
				print (error.code)
				pass
			except BaseException as error:
				repeat = False
				print("caught some other error")
				print('An exception occurred: {}'.format(error))
				pass	
		'''
'''
		print("start sleep")
		time.sleep(5)
		print("end sleep")
		name = battletags[h]
		win_rate = data['us']['stats']['competitive']['overall_stats']['win_rate']
		tier = data['us']['stats']['competitive']['overall_stats']['tier']
		level = data['us']['stats']['competitive']['overall_stats']['level']
		skill_rank = data['us']['stats']['competitive']['overall_stats']['comprank']
		h = h+15
		topPlayer = TopPlayer(h, name, win_rate, tier, level, skill_rank )
		print("-", h, name, win_rate, tier, level, skill_rank)

		db.session.add(topPlayer)
		db.session.commit()
		print("committed" + name)
'''
hero_id_dict = {'Ana':1, 'Bastion':2, 'D.Va':3, 'Genji':4, 'Hanzo':5, 'Junkrat':6, 'Lúcio':7, 'McCree':8, 'Mei':9, 'Mercy':10, 'Pharah':11, 'Reaper':12, 'Reinhardt':13, 'Roadhog':14, 'Soldier: 76':15, 'Symmetra':16, "Torbjörn":17, 'Tracer':18, 'Widowmaker':19, 'Winston':20, 'Zarya':21, 'Zenyatta':22, 'Sombra':23, 'Orisa':24}
players = ['Rexarthur-1739', 'Fantasy-11815', 'Hero-15305', 'SonnyBoy-11601', 'QuickShot-1778', 'Kroi-11847', 'Josiah-11900', 'Clashica-1527', 'Trill-1509', 'Lynxa-11256', 'CSacc-1400', 'Aerrow-11231', 'ricepaper-11726', 'Josh-11682', 'Cinelli-11393', 'Kryptsm-1905', 'RagingTide-1672', 'Vez-11616', 'FAwiN-1442', 'Spoo-1537', 'StayTaded-1734', 'Idree-1229', 'Gerorigh-1294', 'AceStar-11449', 'Quiet-11601', 'Alex-116449', 'Alixxa-11973', 'feeltherain-11126', 'Woodymaker-11351', 'KayosDPS-1453', 'Exziled-1656', 'Femutho-1501', 'WoomyLuma-1961', 'ViBE-22959', 'uwu-11264', 'daddydylan-11182', 'Kitty-13523', 'Mori-11917', 'AntonioACS-1602', 'WardenKat-1922', 'Emerald-11853', 'XAV-11575', 'tycoonbelle-1224', 'CHEERISS-1594', 'Bob-19437', 'Bakuro-11758', 'Zenotna-1446', 'floppynub-1504', 'Stattic-11945', 'Kodzo-1620', 'Cobalt-11296', 'Dizian-1328', 'Zombee-11210', 'IcePrincess-11750', 'Techei-1177', 'mio-2678', 'woodymebid-1313', 'Skumstro-1879', 'Supersmash-1192', 'ImNoPro-1620', 'Produx-11837', 'HimynameisTY-11874', 'Roosty-11838', 'PrinceMO-11110', 'DerekWing-1780', 'STILLHUMAN-21369', 'Robokiller87-1225', 'Burshee-1489', 'STAR2D2-11863', 'jayvix-1346', 'KillerWolfe-1952', 'mio-2678', 'Kyatheir-1533', 'idkkk-1107', 'RichieBooBoo-1782', 'soulward-11370', 'Bnetplayer-152763', 'MrCrowbar-11164', 'Fate-12144', 'Alex-115796', 'Muphin-11785', 'YesimRJ-1902', 'Forever2cv-1391', 'JesusIsLord-11706', 'loMe-1473', 'Dom-12283', 'CritMagnet-11229', 'supejc-1217', 'Muraky-1612', 'Warcrimelol-1884', 'Kupo-1380', 'KIWIo3o-1540', 'Rabidcoyote-11263', 'Silos-11646', 'Avocado-12537', 'Exziled-1656', 'Yorunokage-2191', 'Felicity-11283', 'Fridge-1950', 'LineofSight-1378', 'NatTheGnat-1415', 'WildWolf-125405', 'JohnnyRocket-11570', 'Benene-11203', 'Kormit-1352', 'Ronin-12937', 'Ripperc100jr-1304', 'bleach-12215', 'ZeroX-1243', 'Aura-11385', 'WardenKat-1922', 'KevNoov-1152', 'MofoMan2000-1452', 'Fabstion-1437', 'Cake-11505', 'Lepus-11868', 'Phyx-11632', 'Helix-11269', 'Moookayla-1823', 'Adeeza-1151', 'Krahvin-1702', 'Hypnottikz-1846', 'Yuedar-1391', 'Peter-12547', 'sxn-11118', 'Sumopigman-1853', 'OtakuMark-1962', 'Ceroz-1113', 'Goo-1449', 'Valorthe4th-1108', 'Danaj-1760', 'Ac3Killaz-1849', 'Areitsu-11604', 'Mystic4lLINK-2227', 'Rayzenz-1654', 'Alamer-1561', 'Bree-1146', 'Bakuro-11758', 'ArsenicBeast-1974', 'Erksum-11344', 'Radiculous-11274', 'Zileve-1622', 'ImEricForman-1993', 'Ekingis-1867', 'Baxter-1248', 'Pandamonium-1623', 'dva-11164', 'aien-1262', 'FeistyMercy-1483', 'ForrestJump-11854', 'APandaSniper-1979', 'icecreamboi-11290', 'bad-11909', 'Andrew-13530', 'Shadeslayers-1420', 'Liccdicc420-1773', 'KyungSmooch-1692', 'SilentArcher-1755', 'Solecord-1984', 'Jessiz94-1244', 'Avilore-11382', 'Bonzibon-2123', 'Jacobro-11459', 'Austin-1607', 'Ploof-11842', 'lapengu-1878', 'Battleoid-1337', 'CUBELICIOUS-1176', 'MiniDowgy-1868', 'CobaltB-1834', 'hiddenshadow-1684', 'Migi-21340', 'MudCups-2101', 'TheJumbaco-11481', 'XivuArath-1239', 'TDCarson-1979', 'TDCarson-1979', 'Tigris77-1555', 'Hambi-11117', 'Taz-12110', 'iFlitz-1817', 'Wub-11373', 'Ike7107-1609', 'Valkyrie-12833', 'Huynh-11900', 'Abandon-11850', 'CGDoctor8-1414', 'camboyo-1939', 'iFlitz-1817', 'KcinPt-1610', 'Fury-12786', 'BigDirtyBoy-1827', 'Killerchoose-2845', 'SilverSwim-1752', 'Akichann-1128', 'APandaSniper-1979', 'Bungus-11547', 'Trueglory-1860', 'Yarnx-1597', 'Quasar-12113']
def scrapePlayer():
	akhilstring = "INSERT INTO top_players VALUES ("
	for h in range(0,len(players)):
		try:
			name = players[h]
			playerurl = "https://overwatchtracker.com/profile/pc/us/" + name + "?mode=1"
			req = urllib.request.Request(playerurl, headers={'User-Agent': 'Mozilla/5.0'})
			playerhtml = urllib.request.urlopen(req, context=context)
			#print(playerurl)

			soup = bs4.BeautifulSoup(playerhtml, "html.parser")

			win_rate = soup.find('div', {'data-stat':'Wl'}).text
			KAD = soup.find('div', {'data-stat':'Kad'}).text
			level = soup.find('div', {'data-stat':'Level'}).text
			skill_rank = soup.find('div', {'data-stat':'CompetitiveRank'}).text
			primary_hero = ""
			for hero in soup.findAll('div', {'class':'infobox'}):
				#print(hero)
				for hero2 in soup.findAll('span', {'class':'title'}):
					#print(hero2)
					#print(hero2.text)
					if hero2.text == 'Primary Hero':
						#print("found")
						primary_hero = hero.find('span', {'class':'value'}).text
						#print(primary_hero)
						break;
			#print(primary_hero)
			primary_hero_id = hero_id_dict[primary_hero]
			#print(primary_hero_id)
			#print(f'+ {h+1} {name} {skill_rank} {KAD} {win_rate} {level} {primary_hero_id}')
			
			
			newakhilstring = " ("
			newakhilstring = newakhilstring + str.join(',', (str(h+1), str("\'" + name + "\'"), str("\'" + skill_rank + "\'"), str(KAD), str(win_rate), str(level), str(primary_hero_id)))
			newakhilstring = newakhilstring + "),"
			#print(akhilstring)
			'''
			topPlayer = TopPlayer(h+1, name, skill_rank, KAD, win_rate, level, primary_hero_id)
			db.session.add(topPlayer)
			db.session.commit()
			print("committed" + name)
			'''
			akhilstring = akhilstring + newakhilstring
		except:
			pass
	akhilstring = akhilstring + ");"
	print(akhilstring)
		

 

def main():
	#scrapeHeroes()
	#scrapeAchievements()
	#scrapeEvents()
	#scrapeSkinsItems()
	#scrapeTopPlayers(2)
	scrapePlayer()

if __name__ == "__main__": main()