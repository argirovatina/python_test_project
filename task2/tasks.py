import time
from logger_module import LOG_INFO, LOG_DEBUG
import config
import data_helper

class movementTask():
    
    def __init__(self, uid, bot, move_points, info=''):
        self.uid = uid
        self.status = 'still'
        self.bot = bot
        path = []
        for p in move_points:
            points = p.split(' ')
            path.append(points)
        self.pointpath = path
        self.info = info

    def __process__(self):
        self.move()

    def move(self):
        LOG_DEBUG(self.bot.name, 'Start Moving...')
        self.status = 'moving'
        for point in self.pointpath:
            LOG_DEBUG(self.bot.name, 'New bot position: ' + str(point))
            self.bot.point['x'] = self.bot.gun_point['x'] = point[0]
            self.bot.point['y'] = self.bot.gun_point['y'] = point[1]
            self.bot.point['z'] = self.bot.gun_point['z'] = point[2]
        LOG_DEBUG(self.bot.name, 'Finish moving at position: ' + str(self.pointpath[-1]))

    def teleport(self, x, y, z):
        self.status = 'teleport'
        LOG_DEBUG(self.bot.name, 'Teleport bot on position: %s %s %s' % (x, y, z))
        self.bot.point['x'] = x
        self.bot.point['y'] = y
        self.bot.point['z'] = z
        self.status = 'stil'

class shootTask():

    def __init__(self, *args, **kwargs):
        self.uid = kwargs['uid']
        self.bot = kwargs['bot']
        self.target = kwargs['target_position'].split(' ')
        self.ammoType = kwargs['ammo']
        self.reload = kwargs['reload_time']
        self.shots = kwargs['shotsToKill']
        self.info = kwargs.get('info', 'shootTask #' + str(self.uid))

    def __process__(self):
        self.shootAtTarget()

    def shootAtTarget(self):
        LOG_INFO(self.bot.name, 'Start shoothing at %s by %s shells' % (self.target, self.ammoType))
        if list(set(self.bot.gun_point) & set(self.target)) == []:
            self.status = 'aiming'
            self.bot.gun_point['x'] = self.target[0]
            self.bot.gun_point['y'] = self.target[1]
            self.bot.gun_point['z'] = self.target[2]
            # wait for turret move on target
            time.sleep(2)

        for shootCount in range(1, self.shots+1):
            self.status = 'shooting'
            LOG_DEBUG(self.bot.name, self.ammoType + ' shot #' + str(shootCount))
            self.shoot(self.ammoType)
            self.status = 'reloading'
            time.sleep(self.reload)
            self.status = 'ready'

    def shoot(self, ammoType):
        print config.test_data['shots_types'][str(ammoType)]
           
