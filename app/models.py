from flask import Flask
from flask_sqlalchemy import SQLAlchemy
"""
hero
name,description,role,abilities,availableskins,andavailableitems

achievement
achievement’sname,theheroassociatedwithit(ifapplicable),description,rewardname,rewardtype,andrewardquality

event
Eacheventinstancewillcontainaname,startdate,enddate,skins,anditems

item
name,type,hero,event,andsource

player
name,skillrank,tier,winrate,level,mostplayedchampions,andachievements

skin
name,cost,quality,hero,andevent.
"""

db = SQLAlchemy()

hero_item = db.Table('hero_item',
	db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
	db.Column('item_id', db.Integer, db.ForeignKey('item.id')))

hero_achievement = db.Table('hero_achievement',
	db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')),
	db.Column('achievement_id', db.Integer, db.ForeignKey('achievement.id')))

player_achievement = db.Table('player_achievement',
    db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
    db.Column('achievement_id', db.Integer, db.ForeignKey('achievement.id')))

player_hero = db.Table('player_hero',
	db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
	db.Column('hero_id', db.Integer, db.ForeignKey('hero.id')))


class Hero(db.Model):
	__tablename__ = 'Heros'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable = False)
	description = db.Column(db.String, nullable = False)
	role = db.Column(db.String, nullable = False)
	abilities = db.Column(db.String, nullable = False)
	#foreign key to skins, items

class Achievement(db.Model):
	__tablename__ = 'Achievements'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable = False)
	description = db.Column(db.String, nullable = False)
	reward_name = db.Column(db.String, nullable = True)
	reward_type = db.Column(db.String, nullable = True)
	reward_quality = db.Column(db.String,, nullable = False)

class Event(db.Model):
	__tablename__ = 'Events'

	id = db.Column(db.Integer, primary_key = True)
	start_date = db.Column(db.String, nullable = False)
	end_date = db.Column(db.String, nullable = False)

class Item(db.Model):
	__tablename__ = 'Items'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable = False)
	type = db.Column(db.String, nullable = False)
	source = db.Column(db.String, nullable = True)

class Player(db.Model):
	__tablename__ = 'Players'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable = False)
	rank = db.Column(db.String, nullable = False)
	tier = db.Column(db.String, nullable = False)
	winrate = db.Column(db.Double, nullable = False) #? check if double is valid
	level = db.Column(db.Integer, nullable = False)

class Skin(db.Model):
	__tablename__ = 'Skins'

	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String, nullable = False)
	cost = db.Column(db.Integer, nullable = False)
	quality = db.Column(db.String, nullable = False)
