import urllib.request
import json
import ssl
import time
import os

from html.parser import HTMLParser
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from models import db, Heroes, TopPlayers, Achievements, Events, Skins, Items


indexurl = 'http://boardgameschool.org/LootWatch/index.php?act=picons'
baseurl = 'http://boardgameschool.org/LootWatch/'
context = ssl._create_unverified_context()

Blacklisted = ["Box", "Auxton", "Six-Gun Killer", "Nexus", "Lacroix", "Mexico"]

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        if tag == "img":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "src":
                   if 'heroes' in value:
                   	   #value is halfimageurl and category[2] is folder name
                       category = value.split('/')

                       foldername = category[2]
                       filename = category[len(category)-1]
                       filename = filename.replace("\\", "")
                       print(filename)
                       print(value)
                       print(foldername)
                       if "Torb" not in foldername and "cio" not in foldername and "cioball" not in filename: 
                           imageurl = baseurl + value
                           imageurl = imageurl.replace("\\", "")
                           imageurl = imageurl.replace(" ", "%20")
                           isok = 0
                           for B in Blacklisted:
                               if B in filename:
                                   isok = 1
                                   break;
                           if isok == 0:
                               imageurl = imageurl.replace("x", "%")
                           print(imageurl)
                           req = urllib.request.Request(imageurl, headers={'User-Agent': 'Mozilla/5.0'})
                           theimage = urllib.request.urlopen(req, context=context)

                           #filename = filename.decode('utf-8')
                           print(filename)
                           output = open("../media/items/"+foldername + '/' + filename, 'wb')
                           output.write(theimage.read())
                           output.close()
                       


def scrapeImages():
	req = urllib.request.Request(indexurl, headers={'User-Agent': 'Mozilla/5.0'})
	theimage = urllib.request.urlopen(req, context=context)
	parser = MyHTMLParser()
	parser.feed(str(theimage.read()))

		
		
def main():
	scrapeImages()


if __name__ == "__main__": main()