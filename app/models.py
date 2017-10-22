from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# connect SQLAlchemy and PostgreSQL, use Flask-Migrate (???)

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'   #TThe URI needs to be edited
db = SQLAlchemy(app)




# Join Tables (???) for many to many relationships 


#build classes for each model

class Heroes(db.Model):

	__tablename__ = 'heroes'

	HeroID = db.Column(db.Integer, primary_key = True)
	HeroName = db.Column(db.String, unique = True, nullable = False)
	description = db.Column(db.String, unique = True, nullable = False)
	role = db.Column(db.String, nullable = False)
	Abilities = db.Column(db.String, unique = True, nullable = False)
	Ulti = db.Column(db.String, unique = True, nullable = False)
	
	achievements = db.Relationship('Achievements', backref = 'Heroes',lazy = dynamic)
	skins = db.Relationship('Skins', backref = 'Heroes',lazy = dynamic)


	def __init__(self, HeroName, description, role, A_Ability, B_Ability, Ulti):
		self.HeroName = HeroName
		self.description = description
		self.role = role
		self.A_Ability = A_Ability
		self.B_Ability = B_Ability
		Self.Ulti = Ulti

class TopPlayers(db.Model):

	__tablename__ = 'topPlayers'

	TopPlayerID = db.Column(db.Integer, primary_key = True)
	TopPlayerName = db.Column(db.String, unique = True, nullable = False)
	SkillRank = db.Column(db.String, nullable = False)
	Tier = db.Column(db.String, nullable = False)
	WinRate = db.Column(db.Float, nullable = False)
	Level = db.Column(db.Integer, nullable = False)
	
	heroes = db.Relationship('Heroes', backref = 'TopPlayers',lazy = dynamic)
	achievements = db.Relationship('Achievements', backref = 'TopPlayers',lazy = dynamic)

	def __init__(self, TopPlayerName, SkillRank, Tier, WinRate, Level):
		self.TopPlayerName = TopPlayerName
		self.SkillRank = SkillRank
		self.Tier = Tier
		Self.WinRate = WinRate
		self.Level = Level

class Achievements(db.Model):

	__tablename__ = 'achievements'

	AchievementID = db.Column(db.Integer, primary_key = True)
	AchievementName = db.Column(db.String, unique = True, nullable = False)
	Description = db.Column(db.String, unique = True, nullable = False)
	RewardType = db.Column(db.String, nullable = False)
	RewardQuality = db.Column(db.String, nullable = False)

	
	items = db.Relationship('Items', backref = 'Achievements',lazy = dynamic)
	heroes = db.Relationship('Heroes', backref = 'Achievements',lazy = dynamic)

	def __init__(self, AchievementName, Description, RewardType, RewardQuality):
		self.AchievementName = AchievementName
		self.Description = Description
		self.RewardType = RewardType
		Self.RewardQuality = RewardQuality


class Events(db.Model):

	__tablename__ = 'events'

	EventID = db.Column(db.Integer, primary_key = True)
	EventName = db.Column(db.String, unique = True, nullable = False)
	StartDate = db.Column(db.String, unique = True, nullable = False)
	EndDate = db.Column(db.String, unique = True, nullable = False)
	
	
	skins = db.Relationship('Skins', backref = 'Events',lazy = dynamic)
	items = db.Relationship('Items', backref = 'Events',lazy = dynamic)

	def __init__(self, EventName, StartDate, EndDate):
		self.EventName = EventName
		self.StartDate = StartDate
		self.EndDate = EndDate




class Skins(db.Models):

	__tablename__ = 'skins'

	SkinID = db.Column(db.Integer, primary_key = True)
	SkinName = db.Column(db.String, unique = True, nullable = False)
	Cost = db.Column(db.Integer, nullable = False)
	Quality = db.Column(db.String, nullable = False)
	
	heroes = db.Relationship('Heroes', backref = 'Skins',lazy = dynamic)
	event = db.Relationship('Events	', backref = 'Skins',lazy = dynamic)


	def __init__(self, SkinName, Cost, Quality):
		self.SkinName = SkinName
		self.Cost = Cost
		self.Quality = Quality

class Items(db.Models):

	__tablename__= 'items'

	ItemsID = db.Column(db.Integer, primary_key = True)
	ItemName = db.Column(db.String, unique = True, nullable = False)
	Type = db.Column(db.String, nullable = False)
	
	
	heroes = db.Relationship('Heroes', backref = 'Items',lazy = dynamic)
	achievements = db.Relationship('Achievements', backref = 'Items',lazy = dynamic)
	event = db.Relationship('Events', backref = 'Items',lazy = dynamic)

	def __init__(self, ItemName, Type):
		self.ItemName = ItemName
		self.Type = Type

