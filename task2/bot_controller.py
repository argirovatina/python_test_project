import config
from logger_module import *

class BotController():

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def print_execution_stack(self):
        i = 0
        for task in self.tasks:
            logger.info('BotController, Task # %s task name: %s' % (str(i), str(task.info)))
            i = i + 1

    def run(self):
        logger.debug('BotController, Start runs %d tasks' % len(self.tasks))
        for task in self.tasks:
            logger.info('RUN TASK #%s' % (task.uid))
            task.__process__()
        logger.info('BotController, All tasks finished...')

    def get_task_uid(self):
        config.uid += 1
        return config.uid