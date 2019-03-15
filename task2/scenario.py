import bot_controller
from bot import *
import sys
sys.path.append('test_data')
sys.path.append('logs')
from data_helper import *
from logger_module import *

data = TestData()
bot = Bot()
controller = bot_controller.BotController()
logger.info('~~START~~')
data.prepare_bot(bot),
data.start_battle(bot),

SCENARIO = (
    data.start_first_mission(controller, bot),
    data.shoot_first_target(controller, bot),
    data.start_second_mission(controller, bot),
    data.shoot_second_target(controller, bot),
    data.start_last_mission(controller, bot),
    data.shoot_last_target(controller, bot)
    )

for t in SCENARIO:
    controller.add_task(t)
controller.print_execution_stack()
controller.run()
logger.info('~~FINISH~~')