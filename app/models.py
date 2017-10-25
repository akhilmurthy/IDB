from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# connect SQLAlchemy and PostgreSQL, use Flask-Migrate (???)

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:groupPassword@35.193.209.24/postgres'   #TThe URI needs to be edited
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)




# Join Tables (???) for many to many relationships

hero_top_player = db.Table('hero_top_player',
	db.Column('hero_id',db.Integer, db.ForeignKey('heroes.hero_id')),
	db.Column('top_player_id', db.Integer, db.ForeignKey('top_players.top_player_id')))

achievement_top_player = db.Table('achievement_top_player',
	db.Column('achievement_id',db.Integer, db.ForeignKey('achievements.achievement_id')),
	db.Column('top_player_id', db.Integer, db.ForeignKey('top_players.top_player_id')))

# skin_topPlayer = db.Table('skin_topPlayer',
# 	db.Column('skin_id',db.Integer, db.ForeignKey('skins.SkinID')),
# 	db.Column('topPlayer_id', db.Integer, db.ForeignKey('topPlayers.TopPlayerID')))

hero_item = db.Table('hero_item',
	db.Column('hero_id',db.Integer, db.ForeignKey('heroes.hero_id')),
	db.Column('item_id', db.Integer, db.ForeignKey('items.item_id')))


#build classes for each model

class Hero(db.Model):

	__tablename__ = 'heroes'

	hero_id = db.Column(db.Integer, primary_key = True)
	hero_name = db.Column(db.String, unique = True, nullable = False)
	description = db.Column(db.String, unique = True, nullable = False)
	role = db.Column(db.String, nullable = False)
	abilities = db.Column(db.String, unique = True, nullable = False)
	ulti = db.Column(db.String, unique = True, nullable = False)
	
	# achievements = db.relationship('Achievement', back_populates='heroes')
	achievements = db.relationship('Achievement', backref='Hero',lazy='dynamic')

	skins = db.relationship('Skin', back_populates='heroes')
	items = db.relationship('Item', secondary=hero_item, back_populates='heroes')
	top_players = db.relationship('TopPlayer',secondary = hero_top_player, back_populates='heroes')


	def __init__(self, HeroID, HeroName, description, role, Abilities, Ulti):
		self.hero_id = HeroID
		self.hero_name = HeroName
		self.description = description
		self.role = role
		self.abilities = Abilities
		self.ulti = Ulti

class TopPlayer(db.Model):

	__tablename__ = 'top_players'

	top_player_id = db.Column(db.Integer, primary_key = True)
	top_player_name = db.Column(db.String, unique = True, nullable = False)
	skill_rank = db.Column(db.String, nullable = False)
	tier = db.Column(db.String, nullable = False)
	win_rate = db.Column(db.Float, nullable = False)
	level = db.Column(db.Integer, nullable = False)
	heroes = db.relationship('Hero',secondary = hero_top_player, back_populates='top_players')
	achievements = db.relationship('Achievement', secondary = achievement_top_player, back_populates='top_players')
	# achievements = db.relationship('Achievement',secondary = achievement_top_player, backref = 'TopPlayer',lazy = 'dynamic')

	def __init__(self, TopPlayerID, TopPlayerName, SkillRank, Tier, WinRate, Level):
		self.top_player_id = TopPlayerID
		self.top_player_name = TopPlayerName
		self.skill_rank = SkillRank
		self.tier = Tier
		self.win_rate = WinRate
		self.level = Level

class Achievement(db.Model):

	__tablename__ = 'achievements'

	achievement_id = db.Column(db.Integer, primary_key = True)
	achievement_name = db.Column(db.String, unique = True, nullable = False)
	description = db.Column(db.String, unique = True, nullable = False)
	reward_name = db.Column(db.String)
	reward_type = db.Column(db.String)
	reward_quality = db.Column(db.String)

	
	# items = db.relationship('Item', backref = 'Achievement',lazy = 'dynamic')
	hero_id = db.Column(db.Integer, db.ForeignKey('heroes.hero_id'))
	# heroes = db.relationship('Hero', back_populates='achievements')
	heroes = db.relationship('Hero', backref='Achievement',uselist=False,foreign_keys=[hero_id])
	top_players = db.relationship('TopPlayer', secondary = achievement_top_player, back_populates='achievements')

	def __init__(self, AchievementID, AchievementName, Description, Reward_Name, Reward_Type, Reward_Quality):
		self.achievement_id = AchievementID
		self.achievement_name = AchievementName
		self.description = Description
		self.reward_name = Reward_Name
		self.reward_type = Reward_Type
		self.reward_quality = Reward_Quality


class Event(db.Model):

	__tablename__ = 'events'

	event_id = db.Column(db.Integer, primary_key = True)
	event_name = db.Column(db.String, unique = True, nullable = False)
	start_date = db.Column(db.String, unique = True, nullable = False)
	end_date = db.Column(db.String, unique = True, nullable = False)
	skins = db.relationship('Skin', back_populates='events')	
	items = db.relationship('Item', back_populates='events')

	def __init__(self, EventID, EventName, StartDate, EndDate):
		self.event_id = EventID
		self.event_name = EventName
		self.start_date = StartDate
		self.end_date = EndDate


class Skin(db.Model):

	__tablename__ = 'skins'

	skin_id = db.Column(db.Integer, primary_key = True)
	skin_name = db.Column(db.String, unique = True, nullable = False)
	cost = db.Column(db.Integer)
	quality = db.Column(db.String, nullable = False)
	hero_id= db.Column(db.Integer, db.ForeignKey('heroes.hero_id'))	
	heroes = db.relationship('Hero', back_populates ='skins')
	event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
	events = db.relationship('Event', back_populates = 'skins')


	def __init__(self, SkinID, SkinName, Cost, Quality):
		self.skin_id = SkinID
		self.skin_name = SkinName
		self.cost = Cost
		self.quality = Quality

class Item(db.Model):

	__tablename__= 'items'

	item_id = db.Column(db.Integer, primary_key = True)
	item_name = db.Column(db.String, unique = True, nullable = False)
	item_type = db.Column(db.String, nullable = False)
	event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'))
	events = db.relationship('Event', back_populates = 'items')
	heroes = db.relationship('Hero', secondary=hero_item, back_populates='items')
	
	
	# heroes = db.relationship('Hero', backref = 'Item',lazy = 'dynamic')
	# achievements = db.relationship('Achievement', backref = 'Item',lazy = 'dynamic')
	# event = db.relationship('Event', backref = 'Item',lazy = 'dynamic')

	def __init__(self, ItemID, ItemName, Type):
		self.item_id = ItemID
		self.item_name = ItemName
		self.item_type = Type
