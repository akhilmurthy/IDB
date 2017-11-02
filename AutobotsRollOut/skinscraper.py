import urllib.request
import json
import ssl
import time
import os

from html.parser import HTMLParser
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from models import db, Heroes, TopPlayers, Achievements, Events, Skins, Items


indexurl = 'http://overwatch.wikia.com/wiki/Skin'
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
           imageurl = imageurl.replace("/scale-to-width-down/150", "")
           #print(imageurl)



           #if valid == 1:
           if valid == 1 and "classic" in filename:
               print("---" + filename)
               req = urllib.request.Request(imageurl, headers={'User-Agent': 'Mozilla/5.0'})
               theimage = urllib.request.urlopen(req, context=context)

               output = open("../static/media/skins/"+filename, 'wb')
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