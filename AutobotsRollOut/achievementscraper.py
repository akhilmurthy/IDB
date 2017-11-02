import urllib.request
import json
import ssl
import time
import os
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from models import db, Hero, TopPlayer, Achievement, Event, Skin, Item
#import psycopg2
from html.parser import HTMLParser
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from models import db, Heroes, TopPlayers, Achievements, Events, Skins, Items

baseurl = 'https://overwatch-api.net/api/v1'
indexurl = 'http://overwatch.wikia.com/wiki/Achievements'
context = ssl._create_unverified_context()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "img":
           # Check the list of defined attributes.
           imageurl = ""
           filename = ""
           valid = 0

           for name, value in attrs:
               # If href is defined, print it.
               #print("-"+name)
               if name == "src":
                   imageurl = value
               if name == "\\tdata-image-name":
                   filename = value
                   valid = 1
                   #print("Gotfilename")
           #print(imageurl)
           #print("---"+filename)
           if valid == 1:
               req = urllib.request.Request(imageurl, headers={'User-Agent': 'Mozilla/5.0'})
               theimage = urllib.request.urlopen(req, context=context)
               filename = scrapeAchievements(filename.replace(".png", ""))
               print("00000"+str(filename))
               filename = "%s.png"% (filename)
               output = open("../../media/achievements/"+filename, 'wb')
               output.write(theimage.read())
               output.close()
                       

def scrapeAchievements(findname):

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
    print("--" + findname + "-" + name)
    if findname == name.replace(" ", ""):
      return achievement_id


def scrapeImages():
	req = urllib.request.Request(indexurl, headers={'User-Agent': 'Mozilla/5.0'})
	theimage = urllib.request.urlopen(req, context=context)
	parser = MyHTMLParser()
	parser.feed(str(theimage.read()))

		
		
def main():
	scrapeImages()


if __name__ == "__main__": main()