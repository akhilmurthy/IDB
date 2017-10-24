import urllib.request
import json
import ssl
import time
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from models import db, Heroes, TopPlayers, Achievements, Events, Skins, Items


baseurl = 'https://ugc.masteroverwatch.com/images/skins/'
context = ssl._create_unverified_context()

heronames = ['sombra']
skinnames = ["Peppermint"]

def scrapeImages():
	for hero in heronames:
		for skin in skinnames:
			tempurl = baseurl + hero + '/' + skin + '.jpg'
			try:
				req = urllib.request.Request(tempurl, headers={'User-Agent': 'Mozilla/5.0'})
				theimage = urllib.request.urlopen(req, context=context)
			except:
				pass
			output = open(str(skin + '.jpg'), 'wb')
			output.write(theimage.read())
			output.close()

		
		
def main():
	scrapeImages()


if __name__ == "__main__": main()