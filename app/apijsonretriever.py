import urllib.request
import ssl
import time


baseurl = 'https://overwatch-api.net/api/v1'
context = ssl._create_unverified_context()

'''
url = 'https://overwatch-api.net/api/v1/hero/1'
context = ssl._create_unverified_context()

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
thejson = urllib.request.urlopen(req, context=context)
print(thejson.read())
'''

def scrapeHeroes():
	#24 heroes
	for h in range(1, 25):
	    tempurl = baseurl + '/hero/' + str(h)

	    req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
	    thejson = urllib.request.urlopen(req, context=context)

	    #parse json here
	    #print(thejson.read())

def scrapeAchievements():
	# 73 achievements
	for h in range(1, 74):
	    tempurl = baseurl + '/achievement/' + str(h)

	    req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
	    thejson = urllib.request.urlopen(req, context=context)

	    # parse json here
	    # print(thejson.read())

def scrapeEvents():
	# 3 events. !!! lotta backref from skins and items
	for h in range(1, 4):
	    tempurl = baseurl + '/event/' + str(h)

	    req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
	    thejson = urllib.request.urlopen(req, context=context)

	    # parse json here
	    # print(thejson.read())

def scrapeSkinsItems():
	# 1886 rewards. !!! includes skins and items. parse and identify which it goes into
	for h in range(1, 1887):
	    tempurl = baseurl + '/reward/' + str(h)

	    req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
	    thejson = urllib.request.urlopen(req, context=context)

	    # parse json here
	    # print(thejson.read())

def scrapeTopPlayers():
	battletags = ['SPREE-2984', 'HaventMetYou-2451', 'Hydration-1570', 'zombs-1642', 'Seraphic-21298', 'Jchuk99-1390', 'SumAwsomeKid-1356', 'YLLES-3238', 'SKRRSKRR-1878', 'NotE-1996']
	#top 10 players to start with
	for h in range(0, 10):
	    tempurl = "https://owapi.net/api/v3/u/" + battletags[h] + "/blob"
	    print(tempurl)
	    req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
	    thejson = urllib.request.urlopen(req, context=context)
	    # parse json here
	    #print(thejson.read())
	    time.sleep(2)


def main()
	scrapeHeroes()
	scrapeAchievements()
	scrapeEvents()
	scrapeSkinsItems()
	scrapeTopPlayers()

if __name__ == "__main__": main()


