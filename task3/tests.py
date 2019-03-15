import unittest
import logger
from TankShop import *

class BuyTankTestCase(unittest.TestCase):

	shop = Shop()
	test_palyer = player()
	db = DB()
	fin_logger = fin_logger()

	def test_enough_credits_gold_buyTank(self):
		self.test_palyer.resources.credits = 1000
		self.test_palyer.resources.gold = 25
		self.shop._Shop__buyTank(self.test_palyer, 2101) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 150
			assert gold == 15
			assert self.test_palyer.inventoryPlanes != list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryPlanes, 'test_enough_credits_gold_buyTank')
			raise

	def test_no_credits_no_gold_buyTank(self):
		self.test_palyer.resources.credits = 800
		self.test_palyer.resources.gold = 9
		self.shop._Shop__buyTank(self.test_palyer, 2101)
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 800
			assert gold == 9
			assert self.test_palyer.inventoryPlanes == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryPlanes, 'test_no_credits_no_gold_buyTank')
			raise

	def test_credits_gold_equals_buyTank(self):
		self.test_palyer.resources.credits = 1500
		self.test_palyer.resources.gold = 50
		self.shop._Shop__buyTank(self.test_palyer, 3101) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 0
			assert gold == 0
			assert self.test_palyer.inventoryPlanes == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryPlanes, 'test_credits_gold_equals_buyTank')
			raise

	def test_no_credits_enough_gold_buyTank(self):
		self.test_palyer.resources.credits = 1499
		self.test_palyer.resources.gold = 60
		self.shop._Shop__buyTank(self.test_palyer, 3101) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 1499
			assert gold == 60
			assert self.test_palyer.inventoryPlanes == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryPlanes, 'test_no_credits_enough_gold_buyTank')
			raise

	def test_enough_credits_no_gold_buyTank(self):
		self.test_palyer.resources.credits = 851
		self.test_palyer.resources.gold = 9
		self.shop._Shop__buyTank(self.test_palyer, 2101) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 851
			assert gold == 9
			assert self.test_palyer.inventoryPlanes == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryPlanes, 'test_enough_credits_no_gold_buyTank')
			raise

  	def test_float_credits_buyTank(self):
  		self.test_palyer.resources.credits = 900.0
		self.shop._Shop__buyTank(self.test_palyer, 2101) 
		self.assertIs(self.test_palyer.resources.credits, int)
		self.assertEquals(self.test_palyer.resources.credits, 50)

	def test_float_gold_buyTank(self):
  		self.test_palyer.resources.gold = 15.0
		self.shop._Shop__buyTank(self.test_palyer, 2101) 
		self.assertIs(self.test_palyer.resources.gold, int)
		self.assertEquals(self.test_palyer.resources.gold, 5)
			
	def test_no_tank_id_buyTank(self):
		self.shop._Shop__buyTank(self.test_palyer, 11)
		# should check execpion that tank with such ID doesn't exist

	def test_id_not_int(self):
		self.shop._Shop__buyTank(self.test_palyer, '11')
		# should check execpion that invalid tank ID is provided
			
	def test_credits_gold_equals_buyTank(self):
		self.test_palyer.resources.credits = 1400
		self.test_palyer.resources.gold = 40
		self.shop._Shop__buyTank(self.test_palyer, 3101) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 0
			assert gold == 0
			assert self.test_palyer.inventoryPlanes == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, gold, self.test_palyer.resources.gold, 'test_credits_gold_equals_buyTank')
			raise

class BuyGunsTestCase(unittest.TestCase):

	shop = Shop()
	test_palyer = player()
	db = DB()
	fin_logger = fin_logger()

	def test_inventory_guns_change_buyGuns(self):
		self.shop._Shop__buyGuns(self.test_palyer, 1101, 223)
		self.assertNotEqual(self.test_palyer.inventoryGuns, dict())

	def test_id_not_int_buyGuns(self):
		self.shop._Shop__buyGuns(self.test_palyer, '1101', '223')
		# should check execpion that invalid tank ID and guns ID is provided

	def test_no_tank_id_gun_id_buyGuns(self):
		self.shop._Shop__buyGuns(self.test_palyer, 1, 224)
		self.assertEquals(self.test_palyer.inventoryGuns, dict())

	def test_tank_id_no_gun_id_buyGuns(self):
		self.shop._Shop__buyGuns(self.test_palyer, 2101, 1)
		self.assertEquals(self.test_palyer.inventoryGuns, dict())

	def test_no_tank_id_no_gun_id_buyGuns(self):
		self.shop._Shop__buyGuns(self.test_palyer, 2101, 1)
		self.assertEquals(self.test_palyer.inventoryGuns, dict())

	def test_inventory_not_empty_before_purchase_buyGuns(self):
		self.shop._Shop__buyGuns(self.test_palyer, 2101, 555)
		self.assertNotEquals(self.test_palyer.inventoryPlanes, list())

	def test_tank_list_not_empty_buyGuns(self):
		tankID = 2101
		self.shop._Shop__buyGuns(self.test_palyer, tankID, 555)
		self.assertNotEquals(self.db.guns[tankID], list())		

	def test_enough_credits_gold_buyGuns(self):
		self.test_palyer.resources.credits = 1000
		self.test_palyer.resources.gold = 25
		self.shop._Shop__buyGuns(self.test_palyer, 2101, 555) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 750
			assert gold == 25
			assert self.test_palyer.inventoryGuns != list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryGuns, 'test_enough_credits_gold_buyGuns')
			raise

	def test_no_credits_no_gold_buyGuns(self):
		self.test_palyer.resources.credits = 800
		self.test_palyer.resources.gold = 9
		self.shop._Shop__buyGuns(self.test_palyer, 2101, 655)
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 800
			assert gold == 9
			assert self.test_palyer.inventoryGuns == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryGuns, 'test_no_credits_no_gold_buyGuns')
			raise

	def test_credits_gold_equals_buyGuns(self):
		self.test_palyer.resources.credits = 220
		self.test_palyer.resources.gold = 0
		self.shop._Shop__buyGuns(self.test_palyer, 3101, 485) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 0
			assert gold == 0
			assert self.test_palyer.inventoryGuns == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryGuns, 'test_credits_gold_equals_buyGuns')
			raise

	def test_no_credits_enough_gold_buyGuns(self):
		self.test_palyer.resources.credits = 19
		self.test_palyer.resources.gold = 10
		self.shop._Shop__buyGuns(self.test_palyer, 1101, 224) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 19
			assert gold == 10
			assert self.test_palyer.inventoryGuns == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryGuns, 'test_no_credits_enough_gold_buyGuns')
			raise

	def test_enough_credits_no_gold_buyGuns(self):
		self.test_palyer.resources.credits = 851
		self.test_palyer.resources.gold = 9
		self.shop._Shop__buyGuns(self.test_palyer, 2101, 555) 
		credits = self.test_palyer.resources.credits
		gold = self.test_palyer.resources.gold
		try:
			assert True
			assert credits == 851
			assert gold == 9
			assert self.test_palyer.inventoryPlanes == list()
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, 
				gold, self.test_palyer.resources.gold, self.test_palyer.inventoryPlanes, 'test_enough_credits_no_gold_buyGuns')
			raise

  	def test_float_credits_buyGuns(self):
  		self.test_palyer.resources.credits = 900.0
		self.shop._Shop__buyGuns(self.test_palyer, 1101, 224) 
		self.assertIs(self.test_palyer.resources.credits, int)
		self.assertEquals(self.test_palyer.resources.credits, 50)

	def test_float_gold_buyGuns(self):
  		self.test_palyer.resources.gold = 45.0
		self.shop._Shop__buyGuns(self.test_palyer, 1101, 224) 
		self.assertIs(self.test_palyer.resources.gold, int)
		self.assertEquals(self.test_palyer.resources.gold, 15)

if __name__ == '__main__':
    # begin the unittest.main()		
	log_file = 'logs/log_with_test_results.txt'
   	f = open(log_file, "w")
   	runner = unittest.TextTestRunner(f)
   	unittest.main(testRunner=runner)
   	f.close()   
    