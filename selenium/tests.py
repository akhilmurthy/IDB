import unittest
from unittest import main
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

class GUITestCase(unittest.TestCase):

    def setUp(cls):
        cls.driver = webdriver.Firefox()


    def testPageTitle(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        title = self.driver.find_element_by_class_name('navbar-brand')
        self.assertIn('OVERWATCHGLAM', title.text)
        self.driver.quit()

    def testHeroesTitle(self):
    	baseURL = 'http://www.overwatchglamour.me/heroes'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Heroes of Overwatch',hero_title.text)
    	self.driver.quit()

    def testPlayerTitle(self):
    	baseURL = 'http://www.overwatchglamour.me/players'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Top Players',hero_title.text)
    	self.driver.quit()

    def testAchievementTitle(self):
    	baseURL = 'http://www.overwatchglamour.me/achievements'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Achievements',hero_title.text)
    	self.driver.quit()

    def testEventTitle(self):
    	baseURL = 'http://www.overwatchglamour.me/events'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Events',hero_title.text)
    	self.driver.quit()


    def testSkinTitle(self):
    	baseURL = 'http://www.overwatchglamour.me/skins'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Skins of Overwatch',hero_title.text)
    	self.driver.quit()

    def testItemTitle(self):
    	baseURL = 'http://www.overwatchglamour.me/items'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Items',hero_title.text)
    	self.driver.quit()

    def testSearch(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        query = self.driver.find_element_by_name('search_str')
        query.send_keys('ana')
        query.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        searches = self.driver.find_elements_by_class_name('text-warning')
        found = False
        for s in searches:
        	if 'Genji' in s.text:
        		found = True
        		break
        self.assertTrue(found)
        self.driver.quit()

    def testSearchUnknown(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        query = self.driver.find_element_by_name('search_str')
        query.send_keys('sdokgsdokfg')
        query.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        searches = self.driver.find_element_by_class_name('text-warning')
        self.assertIn('Search results for sdokgsdokfg', searches.text)
        self.driver.quit()

    def testHeroClick(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        hero = self.driver.find_element_by_link_text('HEROES')
        hero.click()
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Heroes of Overwatch',hero_title.text)
    	self.driver.quit()


    def testPlayerClick(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        hero = self.driver.find_element_by_link_text('TOP PLAYERS')
        hero.click()
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Top Players',hero_title.text)
    	self.driver.quit()


    def testAchievementClick(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        hero = self.driver.find_element_by_link_text('ACHIEVEMENTS')
        hero.click()
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Achievements',hero_title.text)
    	self.driver.quit()


    def testEventClick(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        hero = self.driver.find_element_by_link_text('EVENTS')
        hero.click()
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Events',hero_title.text)
    	self.driver.quit()


    def testSkinClick(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        hero = self.driver.find_element_by_link_text('SKINS')
        hero.click()
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Skins of Overwatch',hero_title.text)
    	self.driver.quit()


    def testItemClick(self):
    	baseURL = 'http://www.overwatchglamour.me'
        while True:
        	try:
        		self.driver.get(baseURL)
        		break
        	except:
        		pass
        self.driver.implicitly_wait(10)
        hero = self.driver.find_element_by_link_text('ITEMS')
        hero.click()
        self.driver.implicitly_wait(10)
    	hero_title = self.driver.find_element_by_class_name('text-warning')
    	self.assertIn('Items',hero_title.text)
    	self.driver.quit()



if __name__ == "__main__":
	main(verbosity=2)
