import logging

class fin_logger:	
		
	def __init__(self):
		self.logger = logging.getLogger('fin_logger')

	def log_state(self, player):
		self.logger.setLevel(logging.INFO)
		handler = logging.FileHandler('log_file.log')
		handler.setLevel(logging.INFO)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
		self.logger.info('Player: %s', player)

	def log_balance_assert(self, a_credit, e_credit, a_gold, e_gold, msg):
		self.logger.setLevel(logging.ERROR)
		handler = logging.FileHandler('test_log_file.log')
		handler.setLevel(logging.ERROR)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
		self.logger.error('Actual credit %d, expected credits %d, actual gold %d, expected gold %d, %s' % (a_credit, e_credit, a_gold, e_gold, msg))