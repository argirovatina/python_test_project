import botController
from bot import *
import os
from time import sleep
import re
import logger_module as log
from data_helper import *
import config

data = TestData()
bot = Bot()
controller = botController.BotController()
data.prepare_bot(bot),
data.start_battle(bot),
data.start_first_mission(controller, bot),

SCENARIO = (
    data.shoot_first_target(controller, bot),
    data.start_second_mission(controller, bot),
    data.shoot_second_target(controller, bot),
    data.start_last_mission(controller, bot),
    data.shoot_last_target(controller, bot)
    )

for t in SCENARIO:
    controller.addTask(t)
controller.printExecutionStack()
controller.run()
LOG_INFO(bot.name, '~~FINISH~~')