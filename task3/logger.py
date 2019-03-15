import logging

class fin_logger:	
		
	def __init__(self):
		self.logger = logging.getLogger('fin_logger')
		self.log_file_path = 'logs/tests_log_file.log'

	def log_state(self, player):
		self.logger.setLevel(logging.INFO)
		handler = logging.FileHandler(self.log_file_path)
		handler.setLevel(logging.INFO)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
		self.logger.info('Player: %s', player)

	def log_balance_assert(self, a_credit, e_credit, a_gold, e_gold, inventory_list, msg):
		self.logger.setLevel(logging.ERROR)
		handler = logging.FileHandler(self.log_file_path)
		handler.setLevel(logging.ERROR)
		formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
		handler.setFormatter(formatter)
		self.logger.addHandler(handler)
		self.logger.error(
			'Actual credit %d, expected credits %d, actual gold %d, expected gold %d, inventory_list %s, %s' 
			% (a_credit, e_credit, a_gold, e_gold, inventory_list, msg))