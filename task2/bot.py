from logger_module import *
from time import sleep

class Bot():
    
    def __init__(self):
        self.name = None
        self.point = self.gun_point = {}
        self.tank = None
        self.login = None
        self.state = None        

    def login_in_hangar(self, user_credentials):
        self.state = 'loginin'
        self.name = self.login = user_credentials['login']
        self.pswd = user_credentials['pass']
        logger.info('Strart loginin Bot %s with login: %s, pswd: %s' % (self.name, self.login, self.pswd))
        sleep(1)
        self.state = 'inHangar'
        logger.info('Bot state: %s' % (self.state))

    def get_tank(self, tank):
        self.state = 'buying tank'
        logger.info('Buying tank: %s' % (tank))
        sleep(2)
        self.tank = tank
        logger.info('%s ... OK' % (self.name))
        self.state = 'inHangar'

    def go_to_battle(self):
        self.state = 'load map'
        logger.info('%s LOADING...' %(self.name))
        sleep(5)
        self.point['x'] = self.gun_point['x'] = 0.0
        self.point['y'] = self.gun_point['y'] = 0.0
        self.point['z'] = self.gun_point['z'] = 0.0
        logger.debug('%s ... OK' %(self.name))
