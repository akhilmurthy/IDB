import os
from models import *
from flask_testing import TestCase

class OverwatchTest(TestCase):

def test_heroes(self):
	testHero = Hero(10000,'test','Im a test', 'support', 'Test power', 'exam')
	db.session.add(testHero)
	db.session.commit()
	self.assertTrue(testHero in heroes)

def test_heroes(self):
	testHero = Hero(1002,'testsa','23432', 'sort', 'Tespwer', 'exm')
	db.session.add(testHero)
	db.session.commit()
	self.assertTrue(testHero in heroes)

def test_top_player(self):
	testPlayer = TopPlayer(10000,'test','the thest','bestest',99.999,9000,15)
	db.session.add(testPlayer)
	db.session.commit()
	self.assertTrue(testPlayer in top_players)

def test_top_player(self):
	testPlayer = TopPlayer(10000,'tes35t','the32423 4thest','be234s23test',9,930,11)
	db.session.add(testPlayer)
	db.session.commit()
	self.assertTrue(testPlayer in top_players)

def test_achievement(self):
	testAchievement = Achievement(21343,'ok','asodkf','asdfokas','sdif','safdio')
	db.session.add(testAchievement)
	db.session.commit()
	self.assertTrue(testAchievement in achievements)

def test_achievement(self):
	testAchievement = Achievement(2132343,'ok324','asod2341kf','asdfo1234kas','sdi52352f','safdi213421342134o')
	db.session.add(testAchievement)
	db.session.commit()
	self.assertTrue(testAchievement in achievements)

def test_event(self):
	testEvent = Event(21343,'ok','asodkf','asdfokas','sdif')
	db.session.add(testEvent)
	db.session.commit()
	self.assertTrue(testEvent in events)

def test_event(self):
	testEvent = Event(21332443,'ok23432','aso232dkf','asdf232okas','sd32234if')
	db.session.add(testEvent)
	db.session.commit()
	self.assertTrue(testEvent in events)


def test_skin(self):
	testSkin = Skin(21343,'ok',5,'asdfokas',15,1)
	db.session.add(testSkin)
	db.session.commit()
	self.assertTrue(testSkin in skins)

def test_skin(self):
	testSkin = Skin(2133443,'ok2342341',52,'asdf23412okas',154,12)
	db.session.add(testSkin)
	db.session.commit()
	self.assertTrue(testSkin in skins)