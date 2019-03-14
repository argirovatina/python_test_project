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
			assert credits == 1000
			assert gold == 1000
			assert self.test_palyer.inventoryPlanes != list(), "Tank ID did not get to inventoryPlanes after buying"
		except AssertionError:
			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, gold, self.test_palyer.resources.gold, 'test_enough_credits_gold_buyTank')

# 	def test_no_credits_no_gold_buyTank(self):
# 		self.test_palyer.resources.credits = 800
# 		self.test_palyer.resources.gold = 9
# 		self.shop._Shop__buyTank(self.test_palyer, 2101)
# 		credits = self.test_palyer.resources.credits
# 		gold = self.test_palyer.resources.gold
# 		try:
# 			assert True
# 			assert credits == 800
# 			assert gold == 9
# 			assert self.test_palyer.inventoryPlanes == list()
# 		except AssertionError:
# 			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, gold, self.test_palyer.resources.gold, 'test_no_credits_no_gold_buyTank')
# 			raise

# 	def test_credits_gold_equals_buyTank(self):
# 		self.test_palyer.resources.credits = 1500
# 		self.test_palyer.resources.gold = 50
# 		self.shop._Shop__buyTank(self.test_palyer, 3101) 
# 		credits = self.test_palyer.resources.credits
# 		gold = self.test_palyer.resources.gold
# 		try:
# 			assert True
# 			assert credits == 0
# 			assert gold == 0
# 			assert self.test_palyer.inventoryPlanes == list()
# 		except AssertionError:
# 			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, gold, self.test_palyer.resources.gold, 'test_credits_gold_equals_buyTank')
# 			raise

# 	def test_no_credits_enough_gold_buyTank(self):
# 		self.test_palyer.resources.credits = 1499
# 		self.test_palyer.resources.gold = 60
# 		self.shop._Shop__buyTank(self.test_palyer, 3101) 
# 		credits = self.test_palyer.resources.credits
# 		gold = self.test_palyer.resources.gold
# 		try:
# 			assert True
# 			assert credits == 1499
# 			assert gold == 60
# 			assert self.test_palyer.inventoryPlanes == list()
# 		except AssertionError:
# 			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, gold, self.test_palyer.resources.gold, 'test_no_credits_enough_gold_buyTank')
# 			raise

# 	def test_enough_credits_no_gold_buyTank(self):
# 		self.test_palyer.resources.credits = 851
# 		self.test_palyer.resources.gold = 9
# 		self.shop._Shop__buyTank(self.test_palyer, 2101) 
# 		credits = self.test_palyer.resources.credits
# 		gold = self.test_palyer.resources.gold
# 		try:
# 			assert True
# 			assert credits == 851
# 			assert gold == 9
# 			assert self.test_palyer.inventoryPlanes == list()
# 		except AssertionError:
# 			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, gold, self.test_palyer.resources.gold, 'test_enough_credits_no_gold_buyTank')
# 			raise

#   	def test_float_credits_buyTank(self):
#   		self.test_palyer.resources.credits = 900.0
# 		self.shop._Shop__buyTank(self.test_palyer, 2101) 
# 		self.assertIs(self.test_palyer.resources.credits, int)
# 		self.assertEquals(self.test_palyer.resources.credits, 50)

# 	def test_float_gold_buyTank(self):
#   		self.test_palyer.resources.gold = 15.0
# 		self.shop._Shop__buyTank(self.test_palyer, 2101) 
# 		self.assertIs(self.test_palyer.resources.gold, int)
# 		self.assertEquals(self.test_palyer.resources.gold, 5)
			
# 	def test_no_tank_id_buyTank(self):
# 		self.shop._Shop__buyTank(self.test_palyer, 11)
# 		# should check execpion that tank with such ID doesn't exist

# 	def test_id_not_int(self):
# 		self.shop._Shop__buyTank(self.test_palyer, '11')
# 		# should check execpion that invalid tank ID is provided
			
# 	def test_credits_gold_equals_buyTank(self):
# 		self.test_palyer.resources.credits = 1400
# 		self.test_palyer.resources.gold = 40
# 		self.shop._Shop__buyTank(self.test_palyer, 3101) 
# 		credits = self.test_palyer.resources.credits
# 		gold = self.test_palyer.resources.gold
# 		try:
# 			assert True
# 			assert credits == 0
# 			assert gold == 0
# 			assert self.test_palyer.inventoryPlanes == list()
# 		except AssertionError:
# 			self.fin_logger.log_balance_assert(credits, self.test_palyer.resources.credits, gold, self.test_palyer.resources.gold, 'test_credits_gold_equals_buyTank')
# 			raise

# class BuyGunsTestCase(unittest.TestCase):

# 	shop = Shop()
# 	test_palyer = player()
# 	db = DB()
# 	fin_logger = fin_logger()

# 	def test_inventory_guns_change_buyTank(self):
# 		self.shop._Shop__buyGuns(self.test_palyer, 1101, 223)
# 		self.assertIsNot(self.test_palyer.inventoryGuns, dict())

# 	def test_id_not_int(self):
# 		self.shop._Shop__buyGuns(self.test_palyer, '1101', '223')
# 		# should check execpion that invalid tank ID and guns ID is provided



if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()		