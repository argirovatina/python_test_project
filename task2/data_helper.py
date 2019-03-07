import logger_module as log
import config
from tasks import *

class TestData():

	def prepare_bot(self, bot):
		log.LOG_INFO('', '~~START~~')
		log.LONG_DEBUG(config.test_data)
		bot.loginInHangar(config.USER_CREDS)
		bot.get_tank(config.test_data['tanks'])

	def start_battle(self, bot):
		bot.goToBattle()

	def start_first_mission(self, controller, bot):
		teleport_point = tuple(config.test_data['movemtPoints'][0].split(' '))
		first_mission_point = movementTask(controller.getTaskUid(), bot, config.test_data['movemtPoints'][1:3], 'move to first battle point')
		first_mission_point.teleport(*teleport_point)

	def shoot_first_target(self, controller, bot):
		task = shootTask(bot=bot, uid=controller.getTaskUid(),
			ammo=config.test_data['shootPoints']['t-26'][2],
	        target_position=config.test_data['shootPoints']['t-26'][0], 
	        info='destroy t-26',
	        reload_time=config.test_data['reloadTime'], 
	        shotsToKill=config.test_data['shootPoints']['t-26'][1])
		return task

	def start_second_mission(self, controller, bot):
		task = movementTask(controller.getTaskUid(), bot, config.test_data['movemtPoints'][2:4])
		return task

	def shoot_second_target(self, controller, bot):	
		task = shootTask(bot=bot, uid=controller.getTaskUid(),
			ammo=config.test_data['shootPoints']['pz4'][2],
	    	target_position=config.test_data['shootPoints']['pz4'][0],
	        reload_time=config.test_data['reloadTime'],
	        shotsToKill=config.test_data['shootPoints']['pz4'][1])
		return task

	def start_last_mission(self, controller, bot):
		task = movementTask(controller.getTaskUid(), bot, config.test_data['movemtPoints'][4:], 'move to last battle point')
		return task

	def shoot_last_target(self, controller, bot):
		task = shootTask(bot=bot, uid=controller.getTaskUid(), 
			ammo=config.test_data['shootPoints']['IS2'][2],
	    	target_position=config.test_data['shootPoints']['IS2'][0], 
	        info='destroy IS2',
	        reload_time=config.test_data['reloadTime'], 
	        shotsToKill=config.test_data['shootPoints']['IS2'][1])	
		return task
