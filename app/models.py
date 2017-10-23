from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# connect SQLAlchemy and PostgreSQL, use Flask-Migrate (???)

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:groupPassword@35.193.209.24/overwatch2'   #TThe URI needs to be edited
db = SQLAlchemy(app)




# Join Tables (???) for many to many relationships

hero_topPlayer = db.Table('hero_topPlayer',
	db.Column('hero_id',db.Integer, db.ForeignKey('Hero.HeroID')),
	db.Column('topPlayer_id', db.Integer, db.ForeignKey('TopPlayer.TopPlayerID')))

achievement_topPlayer = db.Table('achievement_topPlayer',
	db.Column('achievement_id',db.Integer, db.ForeignKey('Achievement.AchievementID')),
	db.Column('topPlayer_id', db.Integer, db.ForeignKey('TopPlayer.TopPlayerID')))

skin_topPlayer = db.Table('skin_topPlayer',
	db.Column('skin_id',db.Integer, db.ForeignKey('Skin.SkinID')),
	db.Column('topPlayer_id', db.Integer, db.ForeignKey('TopPlayer.TopPlayerID')))

hero_item = db.Table('hero_item',
	db.Column('hero_id',db.Integer, db.ForeignKey('Hero.HeroID')),
	db.Column('item_id', db.Integer, db.ForeignKey('Item.ItemID')))


#build classes for each model

class Hero(db.Model):

	__tablename__ = 'heroes'

	HeroID = db.Column(db.Integer, primary_key = True)
	HeroName = db.Column(db.String, unique = True, nullable = False)
	description = db.Column(db.String, unique = True, nullable = False)
	role = db.Column(db.String, nullable = False)
	Abilities = db.Column(db.String, unique = True, nullable = False)
	Ulti = db.Column(db.String, unique = True, nullable = False)
	
	achievements = db.relationship('Achievement', backref = 'Hero',lazy = 'dynamic')
	skins = db.relationship('Skin', backref = 'Hero',lazy = 'dynamic')


	def __init__(self, HeroID, HeroName, description, role, Abilities, Ulti):
		self.HeroID = HeroID
		self.HeroName = HeroName
		self.description = description
		self.role = role
		self.Abilities = Abilities
		Self.Ulti = Ulti

class TopPlayer(db.Model):

	__tablename__ = 'topPlayers'

	TopPlayerID = db.Column(db.Integer, primary_key = True)
	TopPlayerName = db.Column(db.String, unique = True, nullable = False)
	SkillRank = db.Column(db.String, nullable = False)
	Tier = db.Column(db.String, nullable = False)
	WinRate = db.Column(db.Float, nullable = False)
	Level = db.Column(db.Integer, nullable = False)
	
	heroes = db.relationship('Hero', backref = 'TopPlayer',lazy = 'dynamic')
	achievements = db.relationship('Achievement', backref = 'TopPlayer',lazy = 'dynamic')

	def __init__(self, TopPlayerID, TopPlayerName, SkillRank, Tier, WinRate, Level):
		self.TopPlayerID = TopPlayerID
		self.TopPlayerName = TopPlayerName
		self.SkillRank = SkillRank
		self.Tier = Tier
		Self.WinRate = WinRate
		self.Level = Level

class Achievement(db.Model):

	__tablename__ = 'achievements'

	AchievementID = db.Column(db.Integer, primary_key = True)
	AchievementName = db.Column(db.String, unique = True, nullable = False)
	Description = db.Column(db.String, unique = True, nullable = False)
	ItemID = db.Column(db.String)
	SkinID = db.Column(db.String)

	
	items = db.relationship('Item', backref = 'Achievement',lazy = 'dynamic')
	heroes = db.relationship('Hero', backref = 'Achievement',lazy = 'dynamic')

	def __init__(self, AchievementID, AchievementName, Description, ItemID= None, SkinID= None):
		self.AchievementID = AchievementID
		self.AchievementName = AchievementName
		self.Description = Description
		self.ItemID = ItemID
		self.SkinID = SkinID


class Event(db.Model):

	__tablename__ = 'events'

	EventID = db.Column(db.Integer, primary_key = True)
	EventName = db.Column(db.String, unique = True, nullable = False)
	StartDate = db.Column(db.String, unique = True, nullable = False)
	EndDate = db.Column(db.String, unique = True, nullable = False)
	
	
	skins = db.relationship('Skin', backref = 'Event',lazy = 'dynamic')
	items = db.relationship('Item', backref = 'Event',lazy = 'dynamic')

	def __init__(self, EventID, EventName, StartDate, EndDate):
		self.EventID = EventID
		self.EventName = EventName
		self.StartDate = StartDate
		self.EndDate = EndDate




class Skin(db.Model):

	__tablename__ = 'skins'

	SkinID = db.Column(db.Integer, primary_key = True)
	SkinName = db.Column(db.String, unique = True, nullable = False)
	Cost = db.Column(db.Integer)
	Quality = db.Column(db.String, nullable = False)
	
	heroes = db.relationship('Hero', backref = 'Skin',lazy = 'dynamic')
	event = db.relationship('Event	', backref = 'Skin',lazy = 'dynamic')


	def __init__(self, SkinID, SkinName, Cost, Quality):
		self.SkinID = SkinID
		self.SkinName = SkinName
		self.Cost = Cost
		self.Quality = Quality

class Item(db.Model):

	__tablename__= 'items'

	ItemID = db.Column(db.Integer, primary_key = True)
	ItemName = db.Column(db.String, unique = True, nullable = False)
	Type = db.Column(db.String, nullable = False)
	
	
	heroes = db.relationship('Hero', backref = 'Item',lazy = 'dynamic')
	achievements = db.relationship('Achievement', backref = 'Item',lazy = 'dynamic')
	event = db.relationship('Event', backref = 'Item',lazy = 'dynamic')

	def __init__(self, ItemID, ItemName, Type):
		self.ItemID = ItemID
		self.ItemName = ItemName
		self.Type = Type
