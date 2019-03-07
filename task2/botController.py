import time as t
import config
from logger_module import *

class BotController():

    def __init__(self):
        self.tasks = []
        self.working_time = 0
        self.start_time = int(t.time())

    def addTask(self, task):
        self.tasks.append(task)

    #not used
    # def getAllTasks(self):
    #     res = None
    #     if len(self.tasks) > 0:
    #         res = self.tasks
    #     return res

    def printExecutionStack(self):
        i = 0
        for task in self.tasks:
            LOG_INFO('BotController', 'Task #' + str(i) + ' task name: ' + str(task.info))
            i = i + 1

    def run(self):
        LOG_DEBUG('BotController', 'Start runs %d tasks' % len(self.tasks))
        for task in self.tasks:
            print('RUN TASK #' + str(task.uid))
            task.__process__()
        LOG_INFO('BotController', 'All tasks finished...')

    def getTaskUid(self):
        config.uid += 1
        return config.uid