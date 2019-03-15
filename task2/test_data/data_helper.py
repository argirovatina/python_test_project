import yaml
import config
from tasks import *
import credentials

test_data = yaml.load(open("test_data/test_data.yaml", 'r'))

class TestData():

	def prepare_bot(self, bot):
		bot.login_in_hangar(credentials.user)
		bot.get_tank(test_data['tanks'])

	def start_battle(self, bot):
		bot.go_to_battle()

	def start_first_mission(self, controller, bot):
		teleport_point = tuple(test_data['movemtPoints'][0].split(' '))
		first_mission_point = MovementTask(controller.get_task_uid(), bot, test_data['movemtPoints'][1:3], 'move to first battle point')
		first_mission_point.teleport(*teleport_point)
		return first_mission_point

	def shoot_first_target(self, controller, bot):
		task = ShootTask(bot=bot, uid=controller.get_task_uid(),
			ammo=test_data['shootPoints']['t-26'][2],
	        target_position=test_data['shootPoints']['t-26'][0], 
	        info='destroy t-26',
	        reload_time=test_data['reloadTime'], 
	        shotsToKill=test_data['shootPoints']['t-26'][1])
		return task

	def start_second_mission(self, controller, bot):
		task = MovementTask(controller.get_task_uid(), bot, test_data['movemtPoints'][2:4])
		return task

	def shoot_second_target(self, controller, bot):	
		task = ShootTask(bot=bot, uid=controller.get_task_uid(),
			ammo=test_data['shootPoints']['pz4'][2],
	    	target_position=test_data['shootPoints']['pz4'][0],
	        reload_time=test_data['reloadTime'],
	        shotsToKill=test_data['shootPoints']['pz4'][1])
		return task

	def start_last_mission(self, controller, bot):
		task = MovementTask(controller.get_task_uid(), bot, test_data['movemtPoints'][4:], 'move to last battle point')
		return task

	def shoot_last_target(self, controller, bot):
		task = ShootTask(bot=bot, uid=controller.get_task_uid(), 
			ammo=test_data['shootPoints']['IS2'][2],
	    	target_position=test_data['shootPoints']['IS2'][0], 
	        info='destroy IS2',
	        reload_time=test_data['reloadTime'], 
	        shotsToKill=test_data['shootPoints']['IS2'][1])	
		return task
