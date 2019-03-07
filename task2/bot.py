import config
import logger_module as log
from time import sleep

class Bot():
    
    def __init__(self):
        self.name = None
        self.point = self.gun_point = {}
        self.tank = None
        self.login = None
        self.state = None        

    def loginInHangar(self, user_credentials):
        self.state = 'loginin'
        self.name = self.login = user_credentials['login']
        self.pswd = user_credentials['pass']
        log.LOG_INFO(self.name, 'Strart loginin Bot %s with login: %s, pswd: %s' % (self.name, self.login, self.pswd))
        sleep(1)
        self.state = 'inHangar'
        log.LOG_INFO(self.name, 'Bot state: ' + self.state)

    def get_tank(self, tank):
        self.state = 'buying tank'
        log.LOG_INFO(self.name, 'Buying tank: ' + tank)
        sleep(2)
        self.tank = tank
        log.LOG_INFO(self.name, '... OK')
        self.state = 'inHangar'

    def goToBattle(self):
        self.state = 'load map'
        log.LOG_INFO(self.name, 'LOADING...')
        sleep(5)
        self.point['x'] = self.gun_point['x'] = 0.0
        self.point['y'] = self.gun_point['y'] = 0.0
        self.point['z'] = self.gun_point['z'] = 0.0
        log.LOG_DEBUG(self.name, '...OK')
